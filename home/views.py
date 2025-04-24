from django.shortcuts import render, redirect
from home.forms import PizzaForm
from home.models import Pizza
from django.views.generic import DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
def index(request):
    return render(request, 'home/index.html')

def create_pizza(request):
    if request.method == 'POST':
        formPizza = PizzaForm(request.POST)
        if formPizza.is_valid():
            info = formPizza.cleaned_data
            pizza = Pizza(
                name=info.get('name'),  
                size=info.get('size'), 
                price=info.get('price'),
                date_created=info.get('date_created'), 
            )
            pizza.save()
            return redirect('index')
    else:
        formPizza = PizzaForm()

    return render(request, 'home/create_pizza.html', {'formPizza': formPizza})

def pizza_list(request):
    pizzas = Pizza.objects.all()
    return render(request, 'home/pizza_list.html', {'pizzas': pizzas})

def detail_pizza(request, idPizza):
    pizza = Pizza.objects.get(id=idPizza)
    return render(request, 'home/detail_pizza.html', {'pizza': pizza})

class ModelDetailPizza(DetailView):
    model = Pizza
    template_name = 'home/detail_pizza.html'

class ViewUpdatePizza(UpdateView):
    model = Pizza
    template_name = 'home/update_pizza.html'
    fields = ['name', 'size', 'price', 'date_created']
    success_url = reverse_lazy('pizza_list')

class ViewDeletePizza(DeleteView):
    model = Pizza
    template_name = 'home/delete_pizza.html'
    success_url = reverse_lazy('pizza_list')

    