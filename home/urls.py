from django.urls import path
from home.views import index, create_user, users_list

urlpatterns =[
    path('', index, name='index'),
      path('user/', users_list, name='users_list'),
    path('user/create/', create_user, name='create_user'),
]