from django.urls import path
from .views import  ProfileView, UpdateProfileView

urlpatterns = [
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),

    path('update_profile/<int:pk>/',
         UpdateProfileView.as_view(), name='update_profile'),




]
