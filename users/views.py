from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as django_login

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