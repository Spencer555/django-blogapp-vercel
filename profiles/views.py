from django.contrib.auth.mixins import LoginRequiredMixin
from profiles.forms import ProfileForm
from profiles.models import Profile
from django.views.generic import UpdateView, DetailView


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'update_profile.html'
    context_object_name = 'profiles'
    success_url = '/'
    form_class = ProfileForm


class ProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profile.html'
    context_object_name = 'profiles'

    def get_queryset(self):
        qs = Profile.objects.filter(user=self.request.user)
        return qs
