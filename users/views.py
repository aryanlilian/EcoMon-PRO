from django.urls import reverse_lazy
from datetime import datetime
from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Income, Spending, User, Account
from django.contrib.auth.mixins import LoginRequiredMixin
from random import randint
from django.core.mail import EmailMessage
from django.conf import settings
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.views.generic import (
    CreateView, UpdateView, DeleteView, ListView
)
from common.mixins import (
    ObjectCreateListViewMixin, ObjectUpdateViewMixin, ObjectDeleteViewMixin,
    EmailTokenGenerator, IsEmailVerifiedMixin, SendEmailThreadMixin
)
from .models import (
    Income, Spending, Profile,
)
from .forms import (
    UserUpdateForm, ProfileUpdateForm, IncomeCreateForm,
    SpendingCreateForm, AccountCreateForm
)
from common.utils import (
    assembly, percentages_of_incomes, daily_avg,
    max_amount, uidb_token_generator, total_currency_converter,
    max_currency_converter
)
from common.constants import (
    template_titles, help_texts, email_activation,
    messages_text
)


class AccountsListView(LoginRequiredMixin, ListView):
    model = Account
    context_object_name = 'accounts'
    template_name = 'users/accounts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = template_titles['accounts_title']
        context['currency'] = Profile.objects.get(user=self.request.user).currency
        return context

    def get_queryset(self, *args, **kwargs):
        if self.request.user.pro_membership:
            return super().get_queryset(*args, **kwargs).filter(user=self.request.user)
        return super().get_queryset(*args, **kwargs).filter(user=self.request.user).first()


class TotalAccountDashboardView(LoginRequiredMixin, View):
    template_name ='users/dashboard.html'

    def get(self, request, *args, **kwargs):
        date = datetime.now()
        accounts = Account.objects.filter(user=request.user)
        currency = Profile.objects.get(user=request.user).currency
        total_incomes = total_currency_converter(request.user, Income, accounts, currency, date.year, date.month)
        total_spendings = total_currency_converter(request.user, Spending, accounts, currency, date.year, date.month)
        total_savings = round(total_incomes - total_spendings, 2)
        spendings_percent = percentages_of_incomes(total_incomes, total_spendings)
        savings_percent = percentages_of_incomes(total_incomes, total_savings)
        max_income = max_currency_converter(request.user, Income, accounts, currency, date.year, date.month)
        max_spending = max_currency_converter(request.user, Spending, accounts, currency, date.year, date.month)
        context = {
            'title': template_titles['dashboard_title'],
            'currency': currency,
            'total_incomes': total_incomes,
            'total_spendings': total_spendings,
            'total_savings': total_savings,
            'spendings_percent': spendings_percent ,
            'savings_percent': savings_percent,
            'max_income': max_income,
            'max_spending': max_spending,
        }
        return render(request, self.template_name, context)


class DashboardView(LoginRequiredMixin, View):
    template_name ='users/dashboard.html'

    def get(self, request, *args, **kwargs):
        date = datetime.now()
        account = Account.objects.get(id=kwargs['pk'])
        incomes = Income.objects.filter(
            user=request.user, account=account, created_date__year=date.year, created_date__month=date.month
        )
        spendings = Spending.objects.filter(
            user=request.user, account=account, created_date__year=date.year, created_date__month=date.month
        )
        currency = account.currency
        total_incomes, total_spendings = assembly(incomes), assembly(spendings)
        total_savings = total_incomes - total_spendings
        spendings_percent = percentages_of_incomes(total_incomes, total_spendings)
        savings_percent = percentages_of_incomes(total_incomes, total_savings)
        max_income, max_spending = max_amount(incomes), max_amount(spendings)
        context = {
            'title': template_titles['dashboard_title'],
            'account' : account,
            'incomes': incomes,
            'spendings': spendings,
            'currency': currency,
            'total_incomes': total_incomes,
            'total_spendings': total_spendings,
            'total_savings': total_savings,
            'spendings_percent': spendings_percent ,
            'savings_percent': savings_percent,
            'max_income': max_income,
            'max_spending': max_spending,
        }
        return render(request, self.template_name, context)


class ProfileView(LoginRequiredMixin, View):
    template_name = 'users/profile.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        user_update_form = UserUpdateForm(
            request.POST,
            instance=request.user
        )
        profile_update_form = ProfileUpdateForm(
            request.POST, request.FILES,
            instance=request.user.profile
        )
        if user_update_form.is_valid() and profile_update_form.is_valid():
            user_update_form.save()
            profile_update_form.save()
            messages.success(
                request,
                messages_text['profile_updated']
            )
            return redirect('profile')
        context['user_update_form'] = user_update_form
        context['profile_update_form'] = profile_update_form
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        user_update_form = UserUpdateForm(
            instance = self.request.user
        )
        profile_update_form = ProfileUpdateForm(
            instance = self.request.user.profile
        )
        context = {
            'title' : template_titles['profile_title'],
            'user_update_form' : user_update_form,
            'profile_update_form' : profile_update_form,
            'phone_number_help_text' : help_texts['phone_number']
        }
        return context


class IncomesCreateListView(LoginRequiredMixin, ObjectCreateListViewMixin):
    model = Income
    form_class = IncomeCreateForm
    model_name = template_titles['incomes_title']
    color = 'primary'


class SpendingsCreateListView(LoginRequiredMixin, ObjectCreateListViewMixin):
    model = Spending
    form_class = SpendingCreateForm
    model_name = template_titles['spendings_title']
    color = 'danger'


class AccountCreateView(LoginRequiredMixin, CreateView):
    model = Account
    form_class = AccountCreateForm
    template_name = 'users/create-update-list-objects.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['objects'] = Account.objects.filter(user=self.request.user) if self.request.user.pro_membership else Account.objects.filter(user=self.request.user).first()
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AccountUpdateView(LoginRequiredMixin, UpdateView):
    model = Account
    template_name = 'users/create-update-list-objects.html'
    fields = ['name', 'category', 'currency']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['objects'] = Account.objects.filter(user=self.request.user)
        return context

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(user=self.request.user)


class IncomeUpdateView(ObjectUpdateViewMixin):
    model = Income
    model_name = template_titles['incomes_title']


class SpendingUpdateView(ObjectUpdateViewMixin):
    model = Spending
    model_name = template_titles['spendings_title']


class IncomeDeleteView(ObjectDeleteViewMixin):
    model = Income
    success_url = reverse_lazy('incomes')


class SpendingDeleteView(ObjectDeleteViewMixin):
    model = Spending
    success_url = reverse_lazy('spendings')


class ArchiveView(LoginRequiredMixin, View):
    template_name = 'users/archive.html'
    incomes = spendings = accounts = account = None

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        total_incomes = total_spendings = None
        if request.user.pro_membership:
            total_incomes = total_currency_converter(request.user, Income, self.accounts, context['currency'])
            total_spendings = total_currency_converter(request.user, Spending, self.accounts, context['currency'])
        else:
            total_incomes, total_spendings = assembly(self.incomes), assembly(self.spendings)
        context['total_incomes'] = total_incomes
        context['total_spendings'] = total_spendings
        context['total_savings'] = round(total_incomes - total_spendings, 2)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        self.account = Account.objects.get(id=request.POST.get('accountId')) if request.user.pro_membership else Account.objects.filter(user=request.user).first()
        year = datetime.strptime(request.POST.get('year'), '%Y')
        month = datetime.strptime(request.POST.get('month'), '%m')
        self.incomes = Income.objects.filter(
            user=request.user, account=self.account, created_date__year=year.year, created_date__month=month.month
        )
        self.spendings = Spending.objects.filter(
            user=request.user, account=self.account, created_date__year=year.year, created_date__month=month.month
        )
        total_incomes, total_spendings = assembly(self.incomes), assembly(self.spendings)
        context['currency'] = self.account.currency
        context['incomes'] = self.incomes
        context['spendings'] = self.spendings
        context['total_incomes'] = total_incomes
        context['total_spendings'] = total_spendings
        context['total_savings'] = round(total_incomes - total_spendings, 2)
        context['year'] = year
        context['month'] = month
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        self.accounts = Account.objects.filter(user=self.request.user) if self.request.user.pro_membership else None
        self.account = Account.objects.filter(user=self.request.user).first() if not self.request.user.pro_membership else Account.objects.filter(user=self.request.user)
        self.incomes = Income.objects.filter(user=self.request.user) if self.request.user.pro_membership else Income.objects.filter(user=self.request.user, account=self.account)
        self.spendings = Spending.objects.filter(user=self.request.user) if self.request.user.pro_membership else Spending.objects.filter(user=self.request.user, account=self.account)
        context = {
            'currency': Profile.objects.get(user=self.request.user).currency if self.accounts else self.account.currency,
            'title' : template_titles['archive_title'],
            'accounts' : self.accounts,
            'incomes' : self.incomes,
            'spendings' : self.spendings
        }
        return context


class EmailVerificationView(LoginRequiredMixin, IsEmailVerifiedMixin, View):

    def get(self, request, *args, **kwargs):
        fin, body = open('common/emails/email_opt_verification.txt', 'rt'), ''
        activate_url = uidb_token_generator('send-or-verify-email-verification', request)
        subject = email_activation['subject']
        for line in fin:
            body += line.replace('username', request.user.username)
        body += '\n' + activate_url
        to_email = request.user.email
        email = EmailMessage(
            subject,
            body,
            settings.EMAIL_HOST_USER,
            [to_email],
        )
        SendEmailThreadMixin(email).start()
        messages.info(request, email_activation['email_sent'])
        return redirect('dashboard')


class SendOrVerifyEmailVerificationView(LoginRequiredMixin, View):

    def get(self, request, uidb64, token):
        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)
            token_generator = EmailTokenGenerator()
            if not token_generator.check_token(user, token):
                messages.error(request, email_activation['link_used'])
                return redirect('dashboard')
            user.email_verified = True
            user.save()
            messages.success(request, email_activation['email_verified'])
        except Exception as e:
            messages.info(request, 'Something went wrong!')
        return redirect('dashboard')
