from django.test import SimpleTestCase
from django.urls import reverse, resolve
from users.views import (
    register,
    change_password,
    login,
    logout_view,
    UpdateUserView,
)


class TestUsersUrls(SimpleTestCase):

    def test_register_url_resolves(self):
        url = reverse("register")
        self.assertEqual(resolve(url).func, register)

    def test_change_password_url_resolves(self):
        url = reverse("change_password")
        self.assertEqual(resolve(url).func, change_password)

    def test_login_url_resolves(self):
        url = reverse("login")
        self.assertEqual(resolve(url).func, login)

    def test_logout_url_resolves(self):
        url = reverse("logout")
        self.assertEqual(resolve(url).func, logout_view)

    def test_update_user_url_resolves(self):
        url = reverse("update_user", args=[1])
        self.assertEqual(resolve(url).func.view_class, UpdateUserView)
