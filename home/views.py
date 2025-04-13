from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.forms import CreateUser
from home.models import User

def index(request):
    return render(request, 'home/index.html')

def create_user(request):
    if request.method=="POST":
        userForm=CreateUser(request.POST)
        if userForm.is_valid():
            info=userForm.cleaned_data
            info_user=User(name=info.get('name'), email=info.get('email'), is_active=info.get('is_active'))
            info_user.save()
            return redirect('index')
    else:
        userForm=CreateUser()

    return render(request, 'home/create_user.html', {'userForm': userForm})