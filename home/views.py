from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.forms import CreateUser
from home.models import User, Branch, Course



def create_user(request):
    if request.method=="POST":
        userForm=CreateUser(request.POST)
        if userForm.is_valid():
            info=userForm.cleaned_data
            info_user=User(name=info.get('name'), email=info.get('email'), is_active=info.get('is_active'))
            info_user.save()
            return redirect('home:users_list')
    else:
        userForm=CreateUser()

    return render(request, 'home/create_user.html', {'userForm': userForm})

def users_list(request):
    search=request.GET.get("search", None)
    if search:
       users=User.objects.filter(email__icontains=search)
    else:
        users=User.objects.all()
    return render(request, 'home/users_list.html', {'users': users})

def branch_list(request):
    branches = Branch.objects.all()
    return render(request, 'home/branch_list.html', {'branches': branches})

def courses_list(request):
    courses=Course.objects.all()
    return render(request, 'home/courses_list.html', {'courses': courses})