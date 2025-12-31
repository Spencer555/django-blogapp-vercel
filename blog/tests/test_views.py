from django.test import TestCase
from django.urls import reverse
from blog.models import Post
from django.contrib.auth.models import User


class PostViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="creator", password="12345")
        self.post = Post.objects.create(
            title="Test Post", body="Test", creator=self.user)

    def test_post_list_view(self):
        response = self.client.get(reverse("blog-home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post")

    def test_post_detail_view(self):
        response = self.client.get(reverse("post-detail", args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post")
