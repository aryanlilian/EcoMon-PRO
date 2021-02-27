from django.urls import path
from .views import (
    AccountsListView, TotalAccountDashboardView, DashboardView,
    ProfileView, IncomesCreateListView, SpendingsCreateListView,
    AccountCreateView, IncomeUpdateView, SpendingUpdateView,
    AccountUpdateView, IncomeDeleteView, SpendingDeleteView,
    ArchiveView, EmailVerificationView, SendOrVerifyEmailVerificationView
)
from .helpers import (
    chart_area, total_chart_area, chart_pie,
    total_chart_pie
)

urlpatterns = [
    path('accounts/', AccountsListView.as_view(), name='accounts'),
    path('dashboard/', TotalAccountDashboardView.as_view(), name='dashboard-total-account'),
    path('dashboard/<int:pk>/', DashboardView.as_view(), name='dashboard'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('dashboard/incomes-chart-area/', total_chart_area, name='incomes-chart-area-total-account'),
    path('dashboard/incomes-chart-pie/', total_chart_pie, name='incomes-chart-pie-total-account'),
    path('dashboard/spendings-chart-area/', total_chart_area, name='spendings-chart-area-total-account'),
    path('dashboard/spendings-chart-pie/', total_chart_pie, name='spendings-chart-pie-total-account'),
    path('dashboard/incomes-chart-area/<int:pk>/', chart_area, name='incomes-chart-area'),
    path('dashboard/incomes-chart-pie/<int:pk>/', chart_pie, name='incomes-chart-pie'),
    path('dashboard/spendings-chart-area/<int:pk>/', chart_area, name='spendings-chart-area'),
    path('dashboard/spendings-chart-pie/<int:pk>/', chart_pie, name='spendings-chart-pie'),
    path('incomes/new/<int:pk>/', IncomesCreateListView.as_view(), name='incomes'),
    path('spendings/new/<int:pk>/', SpendingsCreateListView.as_view(), name='spendings'),
    path('accounts/new/', AccountCreateView.as_view(), name='add-accounts'),
    path('incomes/update/<int:pk>/account/<int:id>/', IncomeUpdateView.as_view(), name='update-income'),
    path('spendings/update/<int:pk>/account/<int:id>/', SpendingUpdateView.as_view(), name='update-spending'),
    path('accounts/update/<int:pk>/', AccountUpdateView.as_view(), name='update-account'),
    path('incomes/delete/<int:pk>/', IncomeDeleteView.as_view(), name='delete-income'),
    path('spendings/delete/<int:pk>/', SpendingDeleteView.as_view(), name='delete-spending'),
    path('archive/', ArchiveView.as_view(), name='archive'),
    path('verification/', EmailVerificationView.as_view(), name='email-verification'),
    path('send/verification/<uidb64>/<token>/', SendOrVerifyEmailVerificationView.as_view(), name='send-or-verify-email-verification'),
]
