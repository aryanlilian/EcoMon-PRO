from django.urls import path
from .views import (
    DashboardView, ProfileView, IncomesCreateListView,
    SpendingsCreateListView, IncomeUpdateView, SpendingUpdateView,
    IncomeDeleteView, SpendingDeleteView, ArchiveView,
    EmailVerificationView, SendOrVerifyEmailVerificationView
)
from .helpers import (
    incomes_chart_area, incomes_chart_pie, spendings_chart_area,
    spendings_chart_pie,
)

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('dashboard/incomes-chart-area/', incomes_chart_area, name='incomes-chart-area'),
    path('dashboard/incomes-chart-pie/', incomes_chart_pie, name='incomes-chart-pie'),
    path('dashboard/spendings-chart-area/', spendings_chart_area, name='spendings-chart-area'),
    path('dashboard/spendings-chart-pie/', spendings_chart_pie, name='spendings-chart-pie'),
    path('incomes/', IncomesCreateListView.as_view(), name='incomes'),
    path('spendings/', SpendingsCreateListView.as_view(), name='spendings'),
    path('incomes/update/<int:pk>/', IncomeUpdateView.as_view(), name='update-income'),
    path('spendings/update/<int:pk>/', SpendingUpdateView.as_view(), name='update-spending'),
    path('incomes/delete/<int:pk>/', IncomeDeleteView.as_view(), name='delete-income'),
    path('spendings/delete/<int:pk>/', SpendingDeleteView.as_view(), name='delete-spending'),
    path('archive', ArchiveView.as_view(), name='archive'),
    path('verification/', EmailVerificationView.as_view(), name='email-verification'),
    path('send/verification/<uidb64>/<token>/', SendOrVerifyEmailVerificationView.as_view(), name='send-or-verify-email-verification'),
]
