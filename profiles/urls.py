from django.urls import path
from .views import * 

urlpatterns = [
    path('register/', RegisterPage, name='register'),
    path('login/', LoginPage, name='login')
]