from django.urls import path
from home.views import index, create_pizza, pizza_list, ModelDetailPizza, ViewUpdatePizza, ViewDeletePizza

urlpatterns = [
    path('', index, name='index'),
     path('pizzas/', pizza_list, name='pizza_list'),
    path('pizzas/create/', create_pizza, name='create_pizza'),
    # path('pizzas/<int:idPizza>/',detail_pizza , name='detail_pizza'),
     path('pizzas/<int:pk>/', ModelDetailPizza.as_view(), name='detail_pizza'),
    path('pizzas/<int:pk>/uptdate/', ViewUpdatePizza.as_view(), name='update_pizza'),
    path('pizzas/<int:pk>/delete/', ViewDeletePizza.as_view() , name='delete_pizza'),
]