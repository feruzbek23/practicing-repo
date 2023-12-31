from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.



@login_required(login_url='login')
def base(request):
    return render(request, 'base.html')


def home(request):
    return render(request, 'home.html')