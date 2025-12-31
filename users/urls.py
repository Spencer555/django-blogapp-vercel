from django.urls import path

from .views import register, change_password, login, UpdateUserView,  logout_view


urlpatterns = [
    path('register/', register, name='register'),

    path('change_password/', change_password, name='change_password'),

    path('login/', login, name='login'),

    path('logout/', logout_view, name='logout'),

    path('update_user/<int:pk>/', UpdateUserView.as_view(), name='update_user'),


]
