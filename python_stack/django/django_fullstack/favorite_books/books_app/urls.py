from django.urls import path     
from . import views
urlpatterns = [
    path('', views.show_books),
    path('add_book', views.create_book),
    path('add_to_fav/<int:book_id>', views.add_to_fav),
    path('delete_fav/<int:book_id>', views.delete_fav),
    path('<int:book_id>', views.view_one_book),
    path('<int:book_id>/delete_book', views.delete_book),
    path('<int:book_id>/update_book', views.update_book), 

]

