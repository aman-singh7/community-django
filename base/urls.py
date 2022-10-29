from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginUser, name="login"),
    path('register/', views.registerUser, name="register"),
]