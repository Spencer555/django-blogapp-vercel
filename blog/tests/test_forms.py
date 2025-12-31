from django.test import TestCase
from blog.forms import PostForm
from django.contrib.auth.models import User



class TestPostForm(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="creator", password="12345")

    def test_valid_form(self):
        
        form = PostForm(data={"title": "Test Title",
                        "body": "Some content" , "creator":self.user})
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = PostForm(data={"title": ""})
        self.assertFalse(form.is_valid())
