from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.home, name='home')
]