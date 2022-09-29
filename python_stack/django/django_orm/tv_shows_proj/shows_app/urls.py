from django.urls import path     
from . import views
urlpatterns = [
    path('', views.redirect_shows),
    path('shows/', views.index),
    path('shows/new/', views.add_show),
    path('shows/new/add', views.add_new_show),
    path('shows/<int:show_id>/edit', views.display_edit),
    path('shows/<int:show_id>/', views.display_show),
    path('shows/<int:show_id>/update', views.edit_show),
    path('shows/<int:show_id>/delete', views.delete_show),


]