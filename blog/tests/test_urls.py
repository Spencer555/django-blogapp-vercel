from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import HomeView, PostDetailView


class TestUrls(SimpleTestCase):
    def test_post_list_url_resolves(self):
        url = reverse("blog-home")
        self.assertEqual(resolve(url).func.view_class, HomeView)

    def test_post_detail_url_resolves(self):
        url = reverse("post-detail", args=[1])
        self.assertEqual(resolve(url).func.view_class, PostDetailView)
