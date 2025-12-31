from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from users.forms import UserUpdateForm
from django.views.generic import UpdateView
from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    return render(request, 'logout.html')


def register(request):
    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['confirm_password']

        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')

            else:
                user = User.objects.create_user(
                    username, email=email, password=password)
                user.save()
                messages.info(request, 'User Successfully Created.')
                return redirect('login')

        else:
            messages.info(request, 'Passwords Not Matching')
            return redirect('register')

    return render(request, 'register.html')


@login_required
def change_password(request):
    if request.method == 'POST':
        user = request.user
        old_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_new_password']

        if new_password == confirm_password:
            if user.check_password(old_password) == True:
                user.set_password(new_password)
                user.save()
                messages.info(request, 'Password Successfully Changed ')
                return redirect('login')

            else:
                messages.info(request, 'Wrong Password ')

        else:
            messages.info(request, 'Passwords do not match. ')

    return render(request, 'password_change.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('blog-home')

        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')

    return render(request, 'login.html')


class UpdateUserView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'update_user.html'
    context_object_name = 'users'
    success_url = '/'
    form_class = UserUpdateForm

    def form_valid(self, form):
        form.instance.username == self.request.user.username
        return super().form_valid(form)

    def test_func(self):
        user = self.get_object()
        if self.request.user == user:
            return True
        return False
