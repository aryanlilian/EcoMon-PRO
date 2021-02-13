from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from .models import User, Income, Spending, Profile
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from common.constants import error_messages, help_texts
from django.core.files.images import get_image_dimensions


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(), help_text=help_texts['email'])
    first_name = forms.CharField(widget=forms.TextInput(), help_text=help_texts['only_letters'])
    last_name = forms.CharField(widget=forms.TextInput(), help_text=help_texts['only_letters'])
    send_marketing_emails = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    accept_terms_and_conditions = forms.BooleanField(widget=forms.CheckboxInput(), required=False)

    class Meta:
        model = User
        fields = [
            'email',
            'username',
            'first_name',
            'last_name',
            'password1',
            'password2',
            'send_marketing_emails',
            'accept_terms_and_conditions'
        ]


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(), help_text=help_texts['email'])
    first_name = forms.CharField(widget=forms.TextInput(), help_text=help_texts['only_letters'])
    last_name = forms.CharField(widget=forms.TextInput(), help_text=help_texts['only_letters'])
    birth_date = forms.DateField(help_text=help_texts['date'])
    phone_number = PhoneNumberField()

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'birth_date',
            'phone_number',
        ]

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name:
            raise ValidationError(
                error_messages['required'],
                code='first_name_empty'
            )
        if not first_name.isalpha():
            raise ValidationError(
                error_messages['first_name'],
                code='first_name_invalid'
            )
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not last_name:
            raise ValidationError(
                error_messages['required'],
                code='last_name_empty'
            )
        if not last_name.isalpha():
            raise ValidationError(
                error_messages['last_name'],
                code='last_name_invalid'
            )
        return last_name

class ProfileUpdateForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput())
    description = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 5, 'cols': 82}),
        help_text=help_texts['profile_description'],
        required=False
    )

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if not image:
            raise ValidationError(
                error_messages['no_image'],
                code='image_empty'
            )
        else:
            width, height = get_image_dimensions(image)
            if width != 150:
                raise ValidationError(
                    error_messages['profile_image_width'] % width,
                    code='image_invalid_width'
                )
            if height != 150:
                raise ValidationError(
                    error_messages['profile_image_height'] % height,
                    code='image_invalid_height'
                )
        return image

    class Meta:
        model = Profile
        fields = [
            'image',
            'description',
            'currency',
        ]


class IncomeCreateForm(forms.ModelForm):
    name = forms.CharField(
        max_length=50, label='Name',
        help_text=help_texts['obj_name']
    )
    amount = forms.DecimalField(
        max_digits=10,
        decimal_places=3,
        label='Amount',
        help_text=help_texts['obj_amount']
    )
    recurrent = forms.BooleanField(required=False, label='Recurrent?')

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        if amount > 9999999.999:
            raise ValidationError(error_messages['to_large_number'])

    class Meta:
        model = Income
        exclude = [
            'user',
            'created_date'
        ]


class SpendingCreateForm(forms.ModelForm):
    name = forms.CharField(
        max_length=50,
        label='Name',
        help_text=help_texts['obj_name']
    )
    amount = forms.DecimalField(
        max_digits=10,
        decimal_places=3,
        label='Amount',
        help_text=help_texts['obj_amount']
    )
    recurrent = forms.BooleanField(required=False, label='Recurrent?')

    class Meta:
        model = Spending
        exclude = [
            'user',
            'created_date'
        ]
