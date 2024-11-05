from django.urls import path
from .views import UserLoginView, UserRegisterView, UserLogoutView

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='auth-login'),
    path('register/', UserRegisterView.as_view(), name='auth-register'),
    path('logout/', UserLogoutView.as_view(), name='auth-logout'),
]