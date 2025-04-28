from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as django_login
from users.forms import FormRegister, FormEditProfile
from django.contrib.auth.decorators import login_required
from users.models import InfoExtra
from django.views.generic import DetailView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404

def login(request):
    if request.method == 'POST':
        formUser = AuthenticationForm(request, data=request.POST)
        if formUser.is_valid():
            user = formUser.get_user()
            django_login(request, user)
            InfoExtra.objects.get_or_create(user=user)
            return redirect('index')
    else:
        formUser = AuthenticationForm()
    
 
    return render(request, 'users/login.html', {'formUser': formUser})

def register(request):
    if request.method == 'POST':
        formUser = FormRegister(request.POST, request.FILES)
        if formUser.is_valid():
            user = formUser.save(commit=False)  
            user.email = formUser.cleaned_data.get('email')  
            user.save()
            hobbies = formUser.cleaned_data.get('hobbies')
            avatar = formUser.cleaned_data.get('avatar')
            InfoExtra.objects.create(user=user,hobbies=hobbies, avatar=avatar)
            return redirect('login')
    else:
        formUser = FormRegister()
    
    return render(request, 'users/register.html', {'formUser': formUser})

@login_required
def edit_profile(request):
    infoextra = request.user.infoextra
    if request.method == 'POST':
        formUser = FormEditProfile(request.POST, request.FILES, instance=request.user)
        if formUser.is_valid():
            formUser.save()
            avatar = formUser.cleaned_data.get('avatar')  
            hobbies = formUser.cleaned_data.get('hobbies')
            if avatar:  
                infoextra.avatar = avatar  
                 
            if hobbies:
                infoextra.hobbies = hobbies
            infoextra.save()
            
            return redirect('index')
    else:
        formUser = FormEditProfile(initial={'avatar':infoextra.avatar, 'hobbies': infoextra.hobbies} ,instance=request.user)
    
    return render(request, 'users/edit_profile.html', {'formUser': formUser})

class ViewDetailProfile(DetailView):
    model = InfoExtra
    template_name = 'users/detail_profile.html'
    def get_object(self):
       
        user_id = self.kwargs['pk']
        return get_object_or_404(InfoExtra, user__id=user_id)

    