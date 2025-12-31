from django.test import TestCase
from django.contrib.auth.models import User
from users.forms import UserUpdateForm


class UserUpdateFormTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="formuser", email="form@example.com", password="testpass"
        )

    def test_valid_form(self):
        """Form is valid when both username and email are provided"""
        form = UserUpdateForm(
            data={"username": "updateduser", "email": "new@example.com"},
            instance=self.user,
        )
        self.assertTrue(form.is_valid())
        updated = form.save()
        self.assertEqual(updated.username, "updateduser")
        self.assertEqual(updated.email, "new@example.com")

    def test_invalid_form_missing_username(self):
        """Form should fail if username is empty"""
        form = UserUpdateForm(
            data={"username": "", "email": "new@example.com"},
            instance=self.user,
        )
        self.assertFalse(form.is_valid())
        self.assertIn("username", form.errors)



    def test_form_has_custom_widgets(self):
        """Ensure widgets include bootstrap classes"""
        form = UserUpdateForm(instance=self.user)
        self.assertIn("form-control",
                      form.fields["username"].widget.attrs["class"])
        self.assertIn("form-control",
                      form.fields["email"].widget.attrs["class"])
