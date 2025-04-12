from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'home/index.html')

def create_user(request):
    return render(request, 'home/create_user.html')