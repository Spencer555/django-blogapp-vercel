from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class UsersViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="viewuser", email="view@example.com", password="testpass"
        )

    def test_register_view_get(self):
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "register.html")

    def test_login_view_get(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "login.html")

    def test_logout_view(self):
        self.client.login(username="viewuser", password="testpass")
        response = self.client.get(reverse("logout"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "logout.html")

    def test_change_password_view_get(self):
        self.client.login(username="viewuser", password="testpass")
        response = self.client.get(reverse("change_password"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "password_change.html")

    def test_update_user_view_requires_login(self):
        url = reverse("update_user", args=[self.user.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)  # redirect to login
