from django.test import SimpleTestCase
from django.urls import reverse, resolve
from users.views import (
    DashboardView,
    ProfileView,
    IncomesCreateListView,
    SpendingsCreateListView,
    ArchiveView
)
from users.helpers import (
    incomes_chart_area,
    spendings_chart_area,
    incomes_chart_pie,
    spendings_chart_pie
)

class TestUrls(SimpleTestCase):

    def test_dashboard_url_resolves(self):
        url = reverse('dashboard')
        self.assertEquals(resolve(url).func.view_class, DashboardView)

    def test_incomes_chart_area_url_resolves(self):
        url = reverse('incomes-chart-area')
        self.assertEquals(resolve(url).func, incomes_chart_area)

    def test_incomes_chart_pie_url_resolves(self):
        url = reverse('incomes-chart-pie')
        self.assertEquals(resolve(url).func, incomes_chart_pie)

    def test_spendings_chart_area_url_resolves(self):
        url = reverse('spendings-chart-area')
        self.assertEquals(resolve(url).func, spendings_chart_area)

    def test_spendings_chart_pie_url_resolves(self):
        url = reverse('spendings-chart-pie')
        self.assertEquals(resolve(url).func, spendings_chart_pie)

    def test_profile_url_resolves(self):
        url = reverse('profile')
        self.assertEquals(resolve(url).func.view_class, ProfileView)

    def test_incomes_url_resolves(self):
        url = reverse('incomes')
        self.assertEquals(resolve(url).func.view_class, IncomesCreateListView)

    def test_spendings_url_resolves(self):
        url = reverse('spendings')
        self.assertEquals(resolve(url).func.view_class, SpendingsCreateListView)

    def test_archive_url_resolves(self):
        url = reverse('archive')
        self.assertEquals(resolve(url).func.view_class, ArchiveView)
