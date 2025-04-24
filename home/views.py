from django.shortcuts import render, redirect
from home.forms import PizzaForm
from home.models import Pizza
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
                price=info.get('price') 
            )
            pizza.save()
            return redirect('index')
    else:
        formPizza = PizzaForm()

    return render(request, 'home/create_pizza.html', {'formPizza': formPizza})

def pizza_list(request):
    pizzas = Pizza.objects.all()
    return render(request, 'home/pizza_list.html', {'pizzas': pizzas})

