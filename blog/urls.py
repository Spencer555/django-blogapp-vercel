from django.urls import path

from .views import (
    HomeView,
    CreatorsPosts,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)
from . import views

urlpatterns = [
    path('', HomeView.as_view(), name='blog-home'),
     path('user/<str:username>', CreatorsPosts.as_view(), name='creator-posts'),
     path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
     path('post/new/', PostCreateView.as_view(), name='post-create'),
     path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
     path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
