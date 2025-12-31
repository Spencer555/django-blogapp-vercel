
from django.contrib.auth.models import User
from django.test import TestCase
from profiles.models import Profile, profile_pic_path

import os


def user_profile_pic_path(instance, filename):
    return f"profile_pics/{instance.user.username}/{filename}"




class ProfileModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpass")

    def test_profile_created_automatically(self):
        """Check if profile is created when user is created"""
        self.assertTrue(Profile.objects.filter(user=self.user).exists())

    def test_str_method(self):
        profile = self.user.profile
        self.assertEqual(str(profile), "testuser Profile")



    def test_profile_pic_path_function(self):
        user = User.objects.create_user(username='anna', password='password123')
        filename = user_profile_pic_path(user.profile, 'test.jpg')
        self.assertTrue(filename.startswith("profile_pics/"))
