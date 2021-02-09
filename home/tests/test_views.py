from django.test import TestCase, Client
from django.urls import reverse
from home.models import Newsletter
from django.core import mail
from users.models import User


class BaseTest(TestCase):

    def setUp(self):
        self.index_url = reverse('index')
        self.about_url = reverse('about')
        self.contact_url = reverse('contact')
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.newsletter = {
            'email': 'test@test.com'
        }
        mail.send_mail(
            'Subject here', 'Here is the message.',
            'from@example.com', ['to@example.com'],
            fail_silently=False,
        )
        mail.send_mail(
            'Subject here again', 'Here is the message.',
            'from@example.com', ['to@example.com'],
            fail_silently=False,
        )
        self.user = {
            'email': 'testemail@gmail.com',
            'username' : 'testusername',
            'first_name' : 'test',
            'last_name' : 'test',
            'password1' : 'testingpassword123',
            'password2' : 'testingpassword123',
            'accept_terms_and_conditions' : 'True'
        }
        self.unmatching_password_user = {
            'email': 'testemail4@gmail.com',
            'username' : 'testusername7',
            'first_name' : 'test',
            'last_name' : 'test',
            'password1' : 'asdrfghqwe',
            'password2' : 'sadsadsadas',
            'accept_terms_and_conditions' : 'True'
        }
        self.common_password_user = {
            'email': 'testemail4@gmail.com',
            'username' : 'testusername5',
            'first_name' : 'test',
            'last_name' : 'test',
            'password1' : 'password',
            'password2' : 'password',
            'accept_terms_and_conditions' : 'True'
        }
        self.invalid_email_user = {
            'email': 'test.com',
            'username' : 'testusername',
            'first_name' : 'test',
            'last_name' : 'test',
            'password1' : 'testingpassword123',
            'password2' : 'testingpassword123',
            'accept_terms_and_conditions' : 'True'
        }
        self.login_user = {
            'username' : 'testusername',
            'password' : 'testingpassword123'
        }
        self.login_empty_username_user = {
            'username' : '',
            'password' : 'testingpassword123'
        }
        self.login_empty_password_user = {
            'username' : 'testusername',
            'password' : ''
        }
        return super().setUp()


class TestIndexViews(BaseTest):

    def test_index_form_view_GET(self):
        response = self.client.get(self.index_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_index_form_view_POST_adds_newsletter_email(self):
        response = self.client.post(self.index_url, self.newsletter)
        newsletter = Newsletter.objects.first()
        self.assertEquals(response.status_code, 302)
        self.assertEquals(newsletter.email, 'test@test.com')


class TesAboutViews(BaseTest):

    def test_about_template_view_GET(self):
        response = self.client.get(self.about_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/about.html')


class TestContactViews(BaseTest):

    def test_contact_view_GET(self):
        response = self.client.get(self.contact_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/contact.html')

    def test_contact_view_POST_send_mail(self):
        self.assertEquals(len(mail.outbox), 2)
        self.assertEquals(mail.outbox[0].subject, 'Subject here')
        self.assertEquals(mail.outbox[1].subject, 'Subject here again')


class TestUserRegistrationViews(BaseTest):

    def test_user_registration_create_view_GET(self):
        response = self.client.get(self.register_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/auth/register.html')


    def test_user_registration_create_view_POST_adds_new_user_success(self):
        response = self.client.post(self.register_url, self.user, format='text/html')
        user = User.objects.first()
        self.assertEquals(response.status_code, 302)
        self.assertEquals(user.email, 'testemail@gmail.com')
        self.assertEquals(user.username, 'testusername')

    def test_user_registration_create_view_POST_unmatching_password(self):
        response = self.client.post(self.register_url, self.unmatching_password_user, format='text/html')
        self.assertEquals(response.status_code, 200)

    def test_user_registration_create_view_POST_common_password(self):
        response = self.client.post(self.register_url, self.common_password_user, format='text/html')
        self.assertEquals(response.status_code, 200)

    def test_user_registration_create_view_POST_common_password(self):
        response = self.client.post(self.register_url, self.invalid_email_user, format='text/html')
        self.assertEquals(response.status_code, 200)

    def test_user_registration_create_view_POST_taken_email_or_username_user(self):
        self.client.post(self.register_url, self.user, format='text/html')
        response = self.client.post(self.register_url, self.user, format='text/html')
        self.assertEquals(response.status_code, 200)



class TestUserLoginViews(BaseTest):

    def test_user_login_view_GET(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/auth/login.html')

    def test_login_view_POST_success(self):
        self.client.post(self.register_url, self.user, format='text/html')
        response = self.client.post(self.login_url, self.login_user, format='text/html')
        self.assertEquals(response.status_code, 302)

    def test_login_view_POST_empty_username(self):
        self.client.post(self.register_url, self.user, format='text/html')
        response = self.client.post(self.login_url, self.login_empty_username_user, format='text/html')
        self.assertEquals(response.status_code, 200)

    def test_login_view_POST_empty_username(self):
        self.client.post(self.register_url, self.user, format='text/html')
        response = self.client.post(self.login_url, self.login_empty_password_user, format='text/html')
        self.assertEquals(response.status_code, 200)
