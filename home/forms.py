from django import forms
from django.utils.translation import gettext_lazy as _

class CreateUser(forms.Form):
    name= forms.CharField(max_length=20)
    email = forms.EmailField(label=_("Email address"))
    is_active = forms.BooleanField(initial=True, required=False)

class CreateBranch(forms.Form):
    name= forms.CharField(max_length=50)
    country = forms.CharField(max_length=30)
    is_active = forms.BooleanField(initial=True, required=False)
    
class CreateCourse(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea, required=False)
    users_qty = forms.IntegerField(min_value=0, initial=0)
    