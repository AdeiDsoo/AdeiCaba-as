from django.urls import path
from home.views import  create_user, users_list, branch_list, courses_list

app_name="home"

urlpatterns =[
    path('', users_list, name='users_list'),
    path('create/', create_user, name='create_user'),
    path('branches/', branch_list, name='branch_list'),
     path('courses/', courses_list, name='courses_list')
]