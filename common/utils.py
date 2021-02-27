from calendar import monthrange
from datetime import datetime
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from . import mixins
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from currency_converter import CurrencyConverter


def assembly(obj):
    return round(sum(i.amount for i in obj), 2)


def percentages_of_incomes(incomes, obj_sum):
    return round((obj_sum / incomes) * 100, 2) if incomes > 0 else 0


def days_of_month(year, month):
    return monthrange(year, month)[1]


def daily_avg(obj_sum, days):
    return round(obj_sum / days, 2)


def max_amount(objs=None):
    if objs:
        return max(i.amount for i in objs)


def check_recurrent_or_new(user, objs, model, account):
    for item in objs:
        date_test = item.created_date.month == 12
        date = datetime(
            item.created_date.year + 1 if date_test else item.created_date.year,
            1 if date_test else item.created_date.month + 1, item.created_date.day,
            item.created_date.hour, item.created_date.minute, item.created_date.second,
            item.created_date.microsecond
        )
        obj,created = model.objects.get_or_create(
            user=user, account=account, name=item.name, amount=item.amount,
            created_date=date, category=item.category, recurrent=True
        )


def delete_recurrent_object(user, obj, model, account):
    date_test = obj.created_date.month == 12
    date = datetime(
        obj.created_date.year + 1 if date_test else obj.created_date.year,
        1 if date_test else obj.created_date.month + 1, obj.created_date.day,
        obj.created_date.hour, obj.created_date.minute, obj.created_date.second,
        obj.created_date.microsecond
    )
    object = model.objects.get(
        user=user, account=account, name=obj.name, amount=obj.amount,
        created_date=date, category=obj.category, recurrent=True
    )
    object.delete()


def uidb_token_generator(link, request, token=None):
    domain = get_current_site(request).domain
    if token is None:
        uidb64 = urlsafe_base64_encode(force_bytes(request.user.id))
        token_generator = mixins.EmailTokenGenerator()
        relatively_url = reverse(
            link, kwargs={'uidb64' : uidb64, 'token' : token_generator.make_token(request.user)}
        )
    else:
        uidb64 = urlsafe_base64_encode(force_bytes(token))
        relatively_url = reverse(
            link, kwargs={'uidb64' : uidb64}
        )
    activate_url = 'http://' + domain + relatively_url
    return activate_url


def total_currency_converter(user, object, accounts, profile_currency, year=None, month=None, category=None):
    total_sum = 0
    converter = CurrencyConverter()
    for account in accounts:
        if not year and not month:
            filtered_objects = object.objects.filter(user=user, account=account)
        elif not category:
            filtered_objects = object.objects.filter(user=user, account=account, created_date__year=year, created_date__month=month)
        else:
            filtered_objects = object.objects.filter(user=user, account=account, created_date__year=year, created_date__month=month, category=category)
        total_filtered_objects = assembly(filtered_objects)
        total_sum += converter.convert(total_filtered_objects, account.currency, profile_currency)
    return round(total_sum, 2)

def max_currency_converter(user, object, accounts, profile_currency, year, month):
    max_object = 0
    converter = CurrencyConverter()
    for account in accounts:
        filtered_objects = object.objects.filter(user=user, account=account, created_date__year=year, created_date__month=month)
        max_filtered_objects = max_amount(filtered_objects)
        if max_filtered_objects and max_filtered_objects > max_object:
            max_object = converter.convert(max_filtered_objects, account.currency, profile_currency)
    return round(max_object, 2)
