from django.urls import path
from .views import UserRegistrationView, UserLoginView,UserTestToken

urlpatterns = [
    path('register', UserRegistrationView.as_view(), name='user-register'),
    path('login', UserLoginView.as_view(), name='user-login'),
    path('token', UserTestToken.as_view(), name='user-test'),
]
