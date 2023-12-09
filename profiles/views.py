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
from django.test import TestCase


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
    

