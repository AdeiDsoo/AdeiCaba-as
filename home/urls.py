from django.urls import path
from home.views import index, create_pizza, pizza_list

urlpatterns = [
    path('', index, name='index'),
     path('pizzas/', pizza_list, name='pizza_list'),
    path('pizzas/create/', create_pizza, name='create_pizza'),
]