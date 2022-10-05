from urllib import request
from django.shortcuts import render,redirect
from .models import User, Book
from django.contrib import messages



def show_books(request):
    if 'user_id' not in request.session:
        
        return redirect("/") 
    context = {
        "all_the_books": Book.objects.all(),
        'this_user': User.objects.get(id = request.session['user_id']),
    } 

    return render(request,"all_books.html", context)

def create_book(request):
    errors = Book.objects.book_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/books")
    else:
        book = Book.objects.create(title = request.POST['title'], desc = request.POST['desc'], uploaded_by = User.objects.get(id = request.session['user_id']))
        book.liked_by.add(User.objects.get(id = request.session['user_id']))

        return redirect("/books")

def view_one_book(request, book_id):
    

    context = {
        "book": Book.objects.get(id=book_id),
        "all_likes": Book.objects.get(id = book_id).liked_by.all(),
        'this_user': User.objects.get(id = request.session['user_id']),
    }

    return render(request, "one_book.html", context)

def delete_book(request, book_id):
    c = Book.objects.get(id = book_id)
    c.delete()

    return redirect("/books")

def update_book(request, book_id):
    book = Book.objects.get(id = book_id)
    if request.POST['title']:
        book.title = request.POST['title']
    if request.POST['desc']:
        book.desc = request.POST['desc']
    book.save()
    return redirect(f"/books/{book_id}")

def add_to_fav(request, book_id):

    Book.objects.get(id = book_id).liked_by.add(User.objects.get(id = request.session['user_id']))
    
    return redirect("/books")

def delete_fav(request, book_id):

    Book.objects.get(id = book_id).liked_by.remove(User.objects.get(id = request.session['user_id']))
    # user = User.objects.get(id = request.session['user_id'])
    # book = Book.objects.get(id = book_id)
    # user.liked_books.remove(book)
    # User.objects.get(id = request.session['user_id']).liked_books.remove(Book.objects.get(id = book_id))
    
    return redirect(f"/books/{book_id}")



