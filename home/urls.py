from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import UserPasswordResetForm, UserSetPasswordForm
from .views import (
    IndexFormView,
    AboutTemplateView,
    ContactView,
    NewsletterUnsubscribeView,
    UserResgistrationCreateView,
    UserLoginView,
    TermsAndConditionsTemplateView,
    PrivacyPolicyTemplateView,
)

urlpatterns = [
    path('', IndexFormView.as_view(), name='index'),
    path('about/', AboutTemplateView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('unsubsribe/<uidb64>', NewsletterUnsubscribeView.as_view(), name='unsubsribe'),
    path('auth/register/', UserResgistrationCreateView.as_view(), name='register'),
    path('auth/login/', UserLoginView.as_view(), name='login'),
    path('auth/logout/', auth_views.LogoutView.as_view(template_name='home/auth/logout.html'), name='logout'),
    path('auth/password-reset/', auth_views.PasswordResetView.as_view(template_name='home/auth/password_reset.html', form_class=UserPasswordResetForm), name='password_reset'),
    path('auth/password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='home/auth/password_reset_done.html'), name='password_reset_done'),
    path('auth/password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='home/auth/password_reset_confirm.html', form_class=UserSetPasswordForm), name='password_reset_confirm'),
    path('auth/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='home/auth/password_reset_complete.html'), name='password_reset_complete'),
    path('terms-and-conditions/', TermsAndConditionsTemplateView.as_view(), name='terms-and-conditions'),
    path('privacy-policy/', PrivacyPolicyTemplateView.as_view(), name='privacy-policy'),
]
