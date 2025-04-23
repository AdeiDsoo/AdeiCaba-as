from django.urls import path
from home.views import index, create_pizza

urlpatterns = [
    path('', index, name='index'),
    path('pizzas/create/', create_pizza, name='create_pizza'),
]