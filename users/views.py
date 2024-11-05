from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.models import User



# def login(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#

class UserLoginView(View):
    def get(self, request):
        return render(request, 'auth/login.html')

    def post(self, request):
        user_form = AuthenticationForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.get_user()
            login(request, user)
            messages.success(request, "User logged in successfully")
            return redirect('index')

        else:
            messages.warning(request, "username or password error")
            return redirect('auth-login')

class UserRegisterView(View):
    def get(self, request):
        return render(request, 'auth/register.html')

    def post(self, request):

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists")
                return redirect('auth-register')

            else:
                new_user = User(first_name=first_name, last_name=last_name, username=username, email=email)
                new_user.set_password(password1)
                new_user.save()
                messages.success(request, "Created successfully")
                return redirect('auth-login')

        else:
            messages.info(request, "Passwords don't match")
            return redirect('auth-register')


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        messages.info(request, "Logout out successfully")
        return redirect('index')