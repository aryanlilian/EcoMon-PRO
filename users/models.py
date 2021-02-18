from django.db import models
from django import forms
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django.urls import reverse
from django.utils import timezone
from PIL import Image


class User(AbstractUser):
    email = models.EmailField(_('Email'), null=False, blank=False, unique=True)
    first_name = models.CharField(_('First Name'), max_length=100, null=False, blank=False)
    last_name = models.CharField(_('Last Name'), max_length=100, null=False, blank=False)
    birth_date = models.DateField(_('Birth Date'), auto_now_add=False, null=True, blank=True)
    phone_number = PhoneNumberField(_('Phone Number'), null=True, blank=True, unique=True)
    email_verified = models.BooleanField(_('Email Verified'), default=False)
    pro_membership = models.BooleanField(_('Pro Membership'), default=False)
    phone_number_verified = models.BooleanField(_('Phone Number Verified'), default=False)
    send_marketing_emails = models.BooleanField(_('Send marketing emails'), default=False)
    accept_terms_conditions_and_security_policy = models.BooleanField(
        _('Accept Terms and Conditions, Data Security Policy'),
        default=False
    )

    def __str__(self):
        return f'{self.username} - {self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('login')


class Profile(models.Model):

    class Currency(models.TextChoices):
        AED = 'AED', _('AED')
        AUD = 'AUD', _('AUD')
        BRL = 'BRL', _('BRL')
        CAD = 'CAD', _('CAD')
        CHF = 'CHF', _('CHF')
        CLP = 'CLP', _('CLP')
        CNY = 'CNY', _('CNY')
        COP = 'COP', _('COP')
        CZK = 'CZK', _('CZK')
        DKK = 'DKK', _('DKK')
        EUR = 'EUR', _('EUR')
        GBP = 'GBP', _('GBP')
        HKD = 'HKD', _('HKD')
        HUF = 'HUF', _('HUF')
        IDR = 'IDR', _('IDR')
        ILS = 'ILS', _('ILS')
        INR = 'INR', _('INR')
        JPY = 'JPY', _('JPY')
        KRW = 'KRW', _('KRW')
        MDL = 'MDL', _('MDL')
        MXN = 'MXN', _('MXN')
        MYR = 'MYR', _('MYR')
        NOK = 'NOK', _('NOK')
        NZD = 'NZD', _('NZD')
        PHP = 'PHP', _('PHP')
        PLN = 'PLN', _('PLN')
        RON = 'RON', _('RON')
        RUB = 'RUB', _('RUB')
        SAR = 'SAR', _('SAR')
        SEK = 'SEK', _('SEK')
        SGD = 'SGD', _('SGD')
        THB = 'THB', _('THB')
        TRY = 'TRY', _('TRY')
        TWD = 'TWD', _('TWD')
        USD = 'USD', _('USD')
        ZAR = 'ZAR', _('ZAR')

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(_('Avatar'), default='default.jpg', upload_to='profile_pics')
    description = models.TextField(_('Description'), null=True, blank=True)
    created_date = models.DateTimeField(_('Created Date/Time'), auto_now_add=True)
    updated_date = models.DateTimeField(_('Updated Date/Time'), auto_now=True)
    currency = models.CharField(
        _('Currency'), max_length=3, choices=Currency.choices, default=Currency.USD
    )

    def __str__(self):
        return f'{self.user.username}\'s Profile'


class Account(models.Model):

    class Currency(models.TextChoices):
        AED = 'AED', _('AED')
        AUD = 'AUD', _('AUD')
        BRL = 'BRL', _('BRL')
        CAD = 'CAD', _('CAD')
        CHF = 'CHF', _('CHF')
        CLP = 'CLP', _('CLP')
        CNY = 'CNY', _('CNY')
        COP = 'COP', _('COP')
        CZK = 'CZK', _('CZK')
        DKK = 'DKK', _('DKK')
        EUR = 'EUR', _('EUR')
        GBP = 'GBP', _('GBP')
        HKD = 'HKD', _('HKD')
        HUF = 'HUF', _('HUF')
        IDR = 'IDR', _('IDR')
        ILS = 'ILS', _('ILS')
        INR = 'INR', _('INR')
        JPY = 'JPY', _('JPY')
        KRW = 'KRW', _('KRW')
        MDL = 'MDL', _('MDL')
        MXN = 'MXN', _('MXN')
        MYR = 'MYR', _('MYR')
        NOK = 'NOK', _('NOK')
        NZD = 'NZD', _('NZD')
        PHP = 'PHP', _('PHP')
        PLN = 'PLN', _('PLN')
        RON = 'RON', _('RON')
        RUB = 'RUB', _('RUB')
        SAR = 'SAR', _('SAR')
        SEK = 'SEK', _('SEK')
        SGD = 'SGD', _('SGD')
        THB = 'THB', _('THB')
        TRY = 'TRY', _('TRY')
        TWD = 'TWD', _('TWD')
        USD = 'USD', _('USD')
        ZAR = 'ZAR', _('ZAR')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(_('Name'), max_length=200)
    created_date = models.DateTimeField(_('Created Date/Time'), auto_now_add=True)
    updated_date = models.DateTimeField(_('Updated Date/Time'), auto_now=True)
    currency = models.CharField(
        _('Currency'), max_length=3, choices=Currency.choices, default=Currency.USD
    )

    def __str__(self):
        return f'{self.name} - {self.currency}'


class Income(models.Model):

    class IncomeCategory(models.TextChoices):
        SALARY = _('Salary')
        AWARDS = _('Awards')
        GRANTS = _('Grants')
        SALE = _('Sale')
        DIVIDENTS = _('Dividents')
        RENTAL = _('Rental')
        REFUNDS = _('Refunds')
        COUPONS = _('Coupons')
        LOTTERY = _('Lottery')
        CAPITAL = _('Capital')
        INVESTMENTS = _('Investments')
        GIFT = _('Gift')
        OTHERS = _('Others')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='incomes')
    name = models.CharField(_('Name'), max_length=100)
    amount = models.DecimalField(_('Amount'), max_digits=10, decimal_places=3)
    recurrent = models.BooleanField(_('Recurrent Income'), default=False)
    created_date = models.DateTimeField(_('Created Date/Time'), default=timezone.now)
    updated_date = models.DateTimeField(_('Updated Date/Time'), auto_now=True)
    category = models.CharField(
        _('Category'), max_length=11,
        choices=IncomeCategory.choices, default=IncomeCategory.SALARY
    )


    def __str__(self):
        return f'{self.name} - {self.user.username}'

    def get_absolute_url(self):
        return reverse('incomes')

    def update_url(self):
        return reverse('update-income', kwargs={'pk': self.pk})

    def delete_url(self):
        return reverse('delete-income', kwargs={'pk': self.pk})


class Spending(models.Model):

    class SpendingCategory(models.TextChoices):
        UTILITIES = _('Utilities')
        RENT = _('Rent')
        INVOICES = _('Invoices')
        SHOPPING = _('Shopping')
        FOOD = _('Food')
        EDUCATION = _('Education')
        FUN = _('Fun')
        INSETMENT = _('Investment')
        OTHERS = _('Others')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='spendings')
    name = models.CharField(_('Name'), max_length=50)
    amount = models.DecimalField(_('Amount'), max_digits=10, decimal_places=3)
    recurrent = models.BooleanField(_('Recurrent Spending'), default=False)
    created_date = models.DateTimeField(_('Created Date/Time'), default=timezone.now)
    updated_date = models.DateTimeField(_('Updated Date/Time'), auto_now=True)
    category = models.CharField(
        _('Category'), max_length=10,
        choices=SpendingCategory.choices, default=SpendingCategory.UTILITIES
    )


    def __str__(self):
        return f'{self.name} - {self.user.username}'

    def get_absolute_url(self):
        return reverse('spendings')

    def update_url(self):
        return reverse('update-spending', kwargs={'pk': self.pk})

    def delete_url(self):
        return reverse('delete-spending', kwargs={'pk': self.pk})
