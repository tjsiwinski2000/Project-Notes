""" Defines URL patterns for learning_logs."""

from django.urls import path, include

from . import views

app_name = 'accounts'

urlpatterns = [
    # Include defalut auth urls.
    path('', include('django.contrib.auth.urls')),
    # Registration page.
    path('register/', views.register, name='register'),
]
