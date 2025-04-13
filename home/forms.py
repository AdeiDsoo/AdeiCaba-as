from django import forms
from django.utils.translation import gettext_lazy as _

class CreateUser(forms.Form):
    name= forms.CharField(max_length=20)
    email = forms.EmailField(label=_("Email address"))
    is_active = forms.BooleanField(initial=True, required=False)