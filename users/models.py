from django.db import models
from django.contrib.auth.models import User

class InfoExtra(models.Model):
  user=models.OneToOneField(User, on_delete=models.CASCADE)
  avatar=models.ImageField(upload_to='avatars', null=True, blank=True)
  hobbies=models.CharField(max_length=150, null=True, blank=True)