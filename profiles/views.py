from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUser
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from profiles import serializers
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import requests

# Create your views here.

def LoginPage(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username or password is incorrect")
            
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


def LogoutView(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def index(request):
    context ={}
    return render(request, 'base.html', context)

def Quran(request):

    api_url = 'https://tanzil.net/#1:2'
    

    response = requests.get(api_url)
    response.raise_for_status()
    quranic_data = response.json()
    context = JsonResponse({'quranic_verses': quranic_data})

    return render(request, 'quran.html', context)

def education(request):
    context = {}
    return render(request, "education.html", context)


# class HelloApiView(APIView):
#     template_name =  'base.html'
#     serializer_class = serializers.HelloSerializer

#     def get(self, request, format=None):
#         message = "Hello world"
#         return Response(message)
    
#     def post(self, request):
        
#         serializer = self.serializer_class(data=request.data)

#         if serializer.is_valid():
#             name = serializer.validated_data.get('name')
#             context = f"Hello {name}"
#             return Response({'context':context})
#         else:
#             return Response(
#                 serializer.errors,
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#     def put(self, request, pk=None):
#         return Response({'method':"PUT"})
    
#     def patch(self, request, pk=None):
#         return Response({"method":"PATCH"})
    
#     def delete(self, request, pk=None):
#         return Response({'method':'DELETE'})
    

