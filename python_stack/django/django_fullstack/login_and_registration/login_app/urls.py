from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),	 
    path('success', views.show),  
    path('login', views.login), 
    path('register', views.register), 
    path('logout', views.logout), 

]