from django import forms
from .models import Newsletter
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm


class NewsletterForm(forms.ModelForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter Your email'}), label=''
        )

    class Meta:
        model = Newsletter
        exclude = ['subscribed_date']


class UserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class' : 'form-control form-control-user', 'id' : 'exampleInputEmail', 'aria-describedby' : 'emailHelp', 'placeholder' : 'Enter Email Address...'}),
            label=''
        )


class UserSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class' : 'form-control form-control-user', 'id' : 'exampleInputPassword', 'placeholder' : 'Enter a new password'}),
            strip=False,
            label=''
        )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class' : 'form-control form-control-user', 'id' : 'exampleInputPassword', 'placeholder' : 'Confirm password'}),
            strip=False,
            label=''
        )
