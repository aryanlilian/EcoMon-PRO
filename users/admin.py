from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserRegistrationForm
from .models import User, Profile, Account, Income, Spending


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    add_form = UserRegistrationForm
    list_display = ['__str__', 'is_superuser',
                    'is_staff', 'is_active', 'date_joined']

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Phone Number',
            {
                'fields': (
                    'phone_number',
                    'phone_number_verified'
                )
            }
        ),
        (
            'Email Status',
            {
                'fields': (
                    'send_marketing_emails',
                    'email_verified'
                )
            }
        ),
        (
            'Pro Membership',
            {
                'fields': (
                    'pro_membership',
                )
            }
        ),
        (
            'Birth Date',
            {
                'fields': (
                    'birth_date',
                )
            }
        ),
        (
            'Terms & Conditions, Data Security Policy',
            {
                'fields': (
                    'accept_terms_conditions_and_security_policy',
                )
            }
        ),
    )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created_date', 'updated_date',)


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created_date', 'updated_date',)


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created_date', 'updated_date',)


@admin.register(Spending)
class SpendingAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created_date', 'updated_date',)
