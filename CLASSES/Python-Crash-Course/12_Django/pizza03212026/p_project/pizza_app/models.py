from django.db import models

# Create your models here.
class Pizza(models.Model):
    pizza_name = models.CharField(max_length =200)
    date_added = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        """ Return representation of the model """
        return self.pizza_name
    
class Topping(models.Model):
    pizza_name_fkey = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        """ Return representation of the model """
        return self.name
    
# 0322-2026 mistake ? 925pm
# class SpecificToppings(models.Model,id):
#     my_pizza = Pizza.objects.get(id=id)
#     my_pizza_toppings = my_pizza.topping_set.all()
    
#     def __str__(self)
#         """ Return representation of the model """
#         return self.