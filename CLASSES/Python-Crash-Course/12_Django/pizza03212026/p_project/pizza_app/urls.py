"""Defines URL patterns for pizza app """
from django.urls import path,include

from . import views

app_name = 'pizza_app'

urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    path('menu/',views.menu, name ='menu'),
    # Return toppings for selected pizza
    path('pizza_toppings/<int:id>/', views.pizza_toppings,name = 'pizza_toppings'),
]
