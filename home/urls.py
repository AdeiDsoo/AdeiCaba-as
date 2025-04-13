from django.urls import path
from home.views import  create_user, users_list

app_name="home"

urlpatterns =[
      path('', users_list, name='users_list'),
    path('create/', create_user, name='create_user'),
]