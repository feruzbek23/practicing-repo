from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUser
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


# Create your views here.

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return messages.info(request, "Username or password is incorrect")
            
    context = {}
    return render(request, 'login.html', context)


def RegisterPage(request):
    form = CreateUser()
    if request.method == "POST":
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account succesfully created!")
        return redirect('login') 

    context = {'form': form}

    return render(request, 'register.html', context)

def index(request):
    context ={}
    return render(request, 'base.html', context)


class HelloApiView(APIView):

    def get(self, request, format=None):

        return Response({'message': 'Hello World'})
    