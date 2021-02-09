from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.contrib.auth.views import LogoutView
from home.views import (
    IndexFormView,
    AboutTemplateView,
    ContactView,
    UserResgistrationCreateView,
    UserLoginView
)


class TestUrls(SimpleTestCase):

    def test_index_url_resolves(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func.view_class, IndexFormView)

    def test_about_url_resolves(self):
        url = reverse('about')
        self.assertEquals(resolve(url).func.view_class, AboutTemplateView)

    def test_contact_url_resolves(self):
        url = reverse('contact')
        self.assertEquals(resolve(url).func.view_class, ContactView)

    def test_register_url_resolves(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func.view_class, UserResgistrationCreateView)

    def test_login_url_resolves(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func.view_class, UserLoginView)

    def test_logout_url_resolves(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func.view_class, LogoutView)
