from datetime import datetime
from django.shortcuts import redirect
from django.contrib.auth.mixins import AccessMixin
from django.views.generic import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type
from threading import Thread
from users.models import Profile, Account
from django.http import Http404
from .utils import (
    assembly, percentages_of_incomes, days_of_month,
    daily_avg, max_amount, check_recurrent_or_new,
    delete_recurrent_object
)


class ObjectCreateListViewMixin(CreateView):
    model = None
    form_class = None
    model_name = None
    color = None
    template_name = 'users/create-update-list-objects.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        date = datetime.now()
        account = Account.objects.get(id=self.kwargs['pk'])
        obj = self.model.objects.filter(
            user=self.request.user,
            account=account,
            created_date__year=date.year,
            created_date__month=date.month
        )
        recurrent_obj = self.model.objects.filter(
            user=self.request.user, recurrent=True,
            account=account,
            created_date__year=date.year,
            created_date__month=date.month
        )
        currency = account.currency
        if date.month == 1:
            obj_last_month = self.model.objects.filter(
                user=self.request.user,
                account=account,
                created_date__year=date.year - 1,
                created_date__month=date.month + 11
            )
        else:
            obj_last_month = self.model.objects.filter(
                user=self.request.user,
                account=account,
                created_date__year=date.year,
                created_date__month=date.month - 1
            )
        total_obj = assembly(obj)
        total_obj_last_month = assembly(obj_last_month)
        check_recurrent_or_new(self.request.user, recurrent_obj, self.model, account)
        context['title'] = self.model_name
        context['color'] = self.color
        context['account'] = account
        context['objects'] = obj
        context['total_sum'] = total_obj
        context['currency'] = currency
        context['total_sum_last_month'] = total_obj_last_month
        context['date'] = date
        return context

    def form_valid(self, form):
        account = Account.objects.get(id=self.kwargs['pk'])
        form.instance.user = self.request.user
        form.instance.account = account
        return super().form_valid(form)


class ObjectUpdateViewMixin(LoginRequiredMixin, UpdateView):
    model = None
    template_name = 'users/create-update-list-objects.html'
    fields = ['name', 'amount', 'category', 'recurrent']
    model_name = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        account = Account.objects.get(id=self.kwargs['id'])
        date = datetime.now()
        obj = self.model.objects.filter(
            user=self.request.user,
            account=account,
            created_date__year=date.year,
            created_date__month=date.month
        )
        recurrent_objs = self.model.objects.filter(
            user=self.request.user,
            account=account,
            recurrent=True,
            created_date__year=date.year,
            created_date__month=date.month
        )
        currency = account.currency
        if date.month == 1:
            obj_last_month = self.model.objects.filter(
                user=self.request.user,
                account=account,
                created_date__year=date.year - 1,
                created_date__month=date.month + 11
            )
        else:
            obj_last_month = self.model.objects.filter(
                user=self.request.user,
                account=account,
                created_date__year=date.year,
                created_date__month=date.month - 1
            )
        total_obj = assembly(obj)
        total_obj_last_month = assembly(obj_last_month)
        check_recurrent_or_new(self.request.user, recurrent_objs, self.model, account)
        context['title'] = self.model_name
        context['color'] = 'success'
        context['account'] = account
        context['objects'] = obj
        context['total_sum'] = total_obj
        context['currency'] = currency
        context['total_sum_last_month'] = total_obj_last_month
        context['date'] = date
        return context


    def form_valid(self, form):
        account = Account.objects.get(id=self.kwargs['id'])
        current_object_instance = form.save(commit=False)
        old_object = self.model.objects.get(id=current_object_instance.id)
        if old_object.recurrent:
            if not current_object_instance.recurrent:
                delete_recurrent_object(self.request.user, old_object, self.model, account)
        form.instance.user = self.request.user
        form.instance.account = account
        return super().form_valid(form)

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(user=self.request.user)


class ObjectDeleteViewMixin(LoginRequiredMixin, DeleteView):
    model = None
    template_name = 'users/incomes_&_spendings.html'
    success_url = None

    def post(self, request, *args, **kwargs):
        if request.POST.get('deleteNextRecurrentObject', False):
            delete_recurrent_object(request.user, self.get_object(), self.model)
        return super().post(request, *args, **kwargs)

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(user=self.request.user)


class EmailTokenGenerator(PasswordResetTokenGenerator):

    def _make_hash_value(self, user, timestamp):
        return(text_type(user.email_verified) + text_type(user.id) + text_type(timestamp))


class SendEmailThreadMixin(Thread):

    def __init__(self, email):
        self.email = email
        Thread.__init__(self)

    def run(self):
        self.email.send(fail_silently=False)


class IsAuthenticatedMixin(AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('accounts')
        return super().dispatch(request, *args, **kwargs)


class IsSuperuserOrStaffMixin(AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser or not request.user.is_staff:
            raise Http404()
        return super().dispatch(request, *args, **kwargs)


class IsEmailVerifiedMixin(AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        if request.user.email_verified:
            raise Http404()
        return super().dispatch(request, *args, **kwargs)
