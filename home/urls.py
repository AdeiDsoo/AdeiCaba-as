from django.urls import path
from home.views import  create_user, users_list, branch_list, courses_list, create_branch, create_courses
app_name="home"

urlpatterns =[
    path('users/', users_list, name='users_list'),
    path('users/create/', create_user, name='create_user'),
    path('branches/', branch_list, name='branch_list'),
    path('branches/create/', create_branch, name='create_branch'),
    path('courses/', courses_list, name='courses_list'),
    path('courses/create/', create_courses, name='create_courses'),
]