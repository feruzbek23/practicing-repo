from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUser
# Create your views here.

def LoginPage(request):
    context = {}
    return render(request, 'login.html', context)


def RegisterPage(request):
    form = CreateUser()
    if request.method == "POST":
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}

    return render(request, 'register.html', context)