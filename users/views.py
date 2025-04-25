from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as django_login
from users.forms import FormRegister, FormEditProfile
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method == 'POST':
        formUser = AuthenticationForm(request, data=request.POST)
        if formUser.is_valid():
            user = formUser.get_user()
            django_login(request, user)
            return redirect('index')
    else:
        formUser = AuthenticationForm()
    
 
    return render(request, 'users/login.html', {'formUser': formUser})

def register(request):
    if request.method == 'POST':
        formUser = FormRegister(request.POST)
        if formUser.is_valid():
            formUser.save()
            return redirect('login')
    else:
        formUser = FormRegister()
    
    return render(request, 'users/register.html', {'formUser': formUser})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        formUser = FormEditProfile(request.POST, instance=request.user)
        if formUser.is_valid():
            formUser.save()
            return redirect('index')
    else:
        formUser = FormEditProfile(instance=request.user)
    
    return render(request, 'users/edit_profile.html', {'formUser': formUser})