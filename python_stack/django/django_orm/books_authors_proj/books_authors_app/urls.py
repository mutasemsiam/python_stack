from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('add', views.add),  
    path('authors', views.authors), 
    path('books/<int:book_id>', views.book_view),  
    path('authors/<int:author_id>', views.author_view), 
    path('books/<int:book_id>/add', views.add_author_for_book),  
    path('authors/<int:author_id>/add', views.add_book_for_author),  

]