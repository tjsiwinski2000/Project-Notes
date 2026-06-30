from django.shortcuts import render

# Get data from database
from .models import Pizza

# Create your views here.
def index(request):
    """ Pizza Home Page """
    return render(request,'pizza/index.html')

def menu(request):
    """ Show Menu """
    pizza_types = Pizza.objects.all()
    context = {'pizza_types' : pizza_types}
    return render(request,'pizza/menu.html',context)

def pizza_toppings(request,id):
    my_pizza = Pizza.objects.get(id=id)
    my_pizza_toppings = my_pizza.topping_set.all()
    context = {'topping_list' : my_pizza_toppings}
    return render(request, 'pizza/toppings.html',context)