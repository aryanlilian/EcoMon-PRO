from .models import Income, Spending
from common.utils import assembly
from datetime import datetime
from django.http import JsonResponse


def incomes_chart_area_data(request):
    incomes_data = []
    first_income = Income.objects.filter(user=request.user).first()
    last_income = Income.objects.filter(user=request.user).last()
    date_distance = None
    if first_income and last_income:
        date_distance = last_income.created_date - first_income.created_date
    if date_distance and date_distance.days <= 365:
        year, month, checks = first_income.created_date.year, first_income.created_date.month, 12
        while checks:
            date = datetime(year, month, 1)
            if month == 12:
                incomes = Income.objects.filter(user=request.user, created_date__year=year, created_date__month=month)
                incomes_data.append({date.strftime('%b'): assembly(incomes)})
                month = 1
                year += 1
            else:
                incomes = Income.objects.filter(user=request.user, created_date__year=year, created_date__month=month)
                incomes_data.append({date.strftime('%b'): assembly(incomes)})
                month += 1
            checks -= 1
    elif date_distance:
        year, month, checks = last_income.created_date.year - \
            1, last_income.created_date.month + 1, 12
        while checks:
            date = datetime(year, month, 1)
            if month == 12:
                incomes = Income.objects.filter(user=request.user, created_date__year=year, created_date__month=month)
                incomes_data.append({date.strftime('%b'): assembly(incomes)})
                month = 1
                year += 1
            else:
                incomes = Income.objects.filter(user=request.user, created_date__year=year, created_date__month=month)
                incomes_data.append({date.strftime('%b'): assembly(incomes)})
                month += 1
            checks -= 1
    return JsonResponse(incomes_data, safe=False)


def spendings_chart_area_data(request):
    spendings_data = []
    first_spending = Spending.objects.filter(user=request.user).first()
    last_spending = Spending.objects.filter(user=request.user).last()
    date_distance = None
    if first_spending and last_spending:
        date_distance = last_spending.created_date - first_spending.created_date
    if date_distance and date_distance.days <= 365:
        year, month, checks = first_spending.created_date.year, first_spending.created_date.month, 12
        while checks:
            date = datetime(year, month, 1)
            if month == 12:
                spendings = Spending.objects.filter(user=request.user, created_date__year=year, created_date__month=month)
                spendings_data.append({date.strftime('%b'): assembly(spendings)})
                month = 1
                year += 1
            else:
                spendings = Spending.objects.filter(user=request.user, created_date__year=year, created_date__month=month)
                spendings_data.append({date.strftime('%b'): assembly(spendings)})
                month += 1
            checks -= 1
    elif date_distance:
        year, month, checks = last_spending.created_date.year - \
            1, last_spending.created_date.month + 1, 12
        while checks:
            date = datetime(year, month, 1)
            if month == 12:
                spendings = Spending.objects.filter(user=request.user, created_date__year=year, created_date__month=month)
                spendings_data.append({date.strftime('%b'): assembly(spendings)})
                month = 1
                year += 1
            else:
                spendings = Spending.objects.filter(user=request.user, created_date__year=year, created_date__month=month)
                spendings_data.append({date.strftime('%b'): assembly(spendings)})
                month += 1
            checks -= 1
    return JsonResponse(spendings_data, safe=False)


def incomes_chart_pie_data(request):
    incomes = Income.objects.filter(user=request.user, created_date__year=datetime.now().year, created_date__month=datetime.now().month)
    total_incomes = assembly(incomes)
    incomes_data, categories = [], ['Salary', 'Awards', 'Grants', 'Sale', 'Dividents', 'Rental', 'Refunds', 'Coupons', 'Lottery', 'Capital', 'Investments', 'Gift', 'Others']
    for category in categories:
        category_incomes = Income.objects.filter(user=request.user, created_date__year=datetime.now().year, created_date__month=datetime.now().month, category=category)
        total_category_incomes = assembly(category_incomes)
        if total_incomes and total_category_incomes:
            incomes_data.append({category: round((total_category_incomes / total_incomes) * 100, 2)})
    return JsonResponse(incomes_data, safe=False)


def spendings_chart_pie_data(request):
    spendings = Spending.objects.filter(user=request.user, created_date__year=datetime.now().year, created_date__month=datetime.now().month)
    total_spendings = assembly(spendings)
    spendings_data, categories = [], ['Utilities', 'Rent', 'Invoices', 'Shopping', 'Food', 'Education', 'Fun', 'Investment', 'Others']
    for category in categories:
        category_spendings = Spending.objects.filter(user=request.user, created_date__year=datetime.now().year, created_date__month=datetime.now().month, category=category)
        total_category_spendings = assembly(category_spendings)
        if total_spendings and total_category_spendings:
            spendings_data.append({category: round((total_category_spendings / total_spendings) * 100, 2)})
    return JsonResponse(spendings_data, safe=False)
