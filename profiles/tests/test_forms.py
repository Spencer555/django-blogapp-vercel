from django.contrib.auth.models import User
from profiles.forms import ProfileForm
from django.core.files.uploadedfile import SimpleUploadedFile
import uuid
from io import BytesIO
from PIL import Image
from django.test import TestCase

# ---------- Helper ----------
def get_temporary_image():
    """Create an in-memory image for testing"""
    img = Image.new("RGB", (100, 100), color=(255, 0, 0))
    file = BytesIO()
    img.save(file, "JPEG")
    file.seek(0)
    return SimpleUploadedFile("test.jpg", file.read(), content_type="image/jpeg")





class ProfileFormTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="formuser", password="testpass")
        self.profile = self.user.profile

    def test_valid_form(self):
        form = ProfileForm(
            data={},
            files={"image": get_temporary_image()},
            instance=self.profile
        )
        self.assertTrue(form.is_valid())

    