from django.urls import path
from Main.views import  index

app_name="Main"

urlpatterns =[
      path('', index, name='index'),
]