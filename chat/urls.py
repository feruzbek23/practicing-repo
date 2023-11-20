from django.urls import path
from . import views

urlpatterns = [
    path('discuss/', views.lobby, name='lobby')
]