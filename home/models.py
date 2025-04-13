from django.db import models
from django.utils.translation import gettext_lazy as _

class User(models.Model):
    name= models.CharField(max_length=20)
    email = models.EmailField(_("email address"), unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} - {self.email} - {self.created_at} - {self.is_active}'
    
class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    users_qty = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} - {self.users_qty} users - {self.created_at:%Y-%m-%d}'
    
class Branch(models.Model):
    name = models.CharField(max_length=50)
    country=models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f'{self.name} -{self.country} - {self.created_at} - {self.is_active}'