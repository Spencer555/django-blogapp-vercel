from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post


class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="creator", password="12345")
        self.post = Post.objects.create(
            title="Test Post",
            body="Hello World",
            creator=self.user
        )

    def test_post_str_method(self):
        self.assertEqual(str(self.post), "Test Post")

    def test_post_has_creator(self):
        self.assertEqual(self.post.creator.username, "creator")
