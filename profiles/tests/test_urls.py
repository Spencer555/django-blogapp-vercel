from django.test import SimpleTestCase
from django.urls import reverse, resolve

from profiles.views import ProfileView, UpdateProfileView


class TestProfilesUrls(SimpleTestCase):

    def test_profile_url_resolves_to_profile_view(self):
        url = reverse("profile", args=[1])
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, ProfileView)

    def test_update_profile_url_resolves_to_update_profile_view(self):
        url = reverse("update_profile", args=[1])
        resolver = resolve(url)
        self.assertEqual(resolver.func.view_class, UpdateProfileView)
