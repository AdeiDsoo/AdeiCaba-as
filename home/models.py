from django.db import models
from django.utils.translation import gettext_lazy as _

class User(models.Model):
    name= models.CharField(max_length=20)
    email = models.EmailField(_("email address"), unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} - {self.email} - {self.created_at} - {self.is_active}'
    
