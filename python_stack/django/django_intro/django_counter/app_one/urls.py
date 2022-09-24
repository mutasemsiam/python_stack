from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('clear/', views.delete),
    path('add/', views.add),


]
