from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from io import BytesIO
from PIL import Image


# ---------- Helper ----------
def get_temporary_image():
    """Create an in-memory image for testing"""
    img = Image.new("RGB", (100, 100), color=(255, 0, 0))
    file = BytesIO()
    img.save(file, "JPEG")
    file.seek(0)
    return SimpleUploadedFile("test.jpg", file.read(), content_type="image/jpeg")






# ---------- Views Tests ----------
class ProfileViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="viewuser", password="testpass")
        self.profile = self.user.profile

    def test_profile_view_requires_login(self):
        url = reverse("profile", args=[self.profile.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)  # redirect to login

    def test_profile_view_authenticated(self):
        self.client.login(username="viewuser", password="testpass")
        url = reverse("profile", args=[self.profile.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "viewuser")

    def test_update_profile_view_authenticated(self):
        self.client.login(username="viewuser", password="testpass")
        url = reverse("update_profile", args=[self.profile.pk])

        # get_temporary_image already returns a SimpleUploadedFile
        image_file = get_temporary_image()

        response = self.client.post(url, {"image": image_file}, follow=True)

        self.assertEqual(response.status_code, 200)
        self.profile.refresh_from_db()
        self.assertTrue(self.profile.image)

    def test_update_profile_requires_login(self):
        url = reverse("update_profile", args=[self.profile.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)  # redirect to login
