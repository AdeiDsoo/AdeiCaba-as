from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class FormRegister(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput, required=True)
    username = forms.CharField(max_length=30, required=True)
    hobbies = forms.CharField(label='Hobbies', required=False, widget=forms.Textarea)
    avatar = forms.ImageField(label='Avatar', required=False)
class Meta:
    model=User
    fields = ( 'username', 'email', 'password1', 'password2', 'hobbies', 'avatar')
    help_texts = {key:'' for key in fields}

class FormEditProfile(forms.ModelForm):
    password= None
    email= forms.EmailField(required=False)
    first_name= forms.CharField(label='Nombre')
    last_name= forms.CharField(label='Apellido')
    avatar= forms.ImageField(required=False)
    hobbies= forms.CharField(label='Hobbies', required=False, widget=forms.Textarea)

    class Meta:
        model= User
        fields= ('email', 'first_name', 'last_name', 'avatar', 'hobbies')
        
