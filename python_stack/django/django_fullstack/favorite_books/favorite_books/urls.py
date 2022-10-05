from django.urls import path, include

urlpatterns = [
    path('', include('login_app.urls')),
    path('books/', include('books_app.urls')),

]