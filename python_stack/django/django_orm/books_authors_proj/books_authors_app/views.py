
from django.shortcuts import render,redirect
from .models import Book, Author


def index(request):
    context = {
        "all_the_books": Book.objects.all()
    }

    return render(request, "index.html", context)

def add(request):
    if request.POST['add'] == 'book':
        Book.objects.create(title = request.POST['title'], desc = request.POST['desc'])
        return redirect('/')
    
    elif request.POST['add'] == 'author':
        Author.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], notes = request.POST['notes'])
        return redirect('/authors')


def authors(request):
    context = {
        "all_the_authors": Author.objects.all()
    }

    return render(request, "authors.html", context)

def book_view(request, book_id):
    context = {
        "book": Book.objects.get(id=book_id),
        "all_the_authors": Author.objects.all(),
    }

    return render(request, "bookview.html", context)

def author_view(request, author_id):
    context = {
        "author": Author.objects.get(id=author_id),
        "all_the_books": Book.objects.all(),
    }

    return render(request, "authorview.html", context)


def add_author_for_book(request, book_id):
    
    Book.objects.get(id=book_id).authors.add(Author.objects.get(id = request.POST['which_author']))

    return redirect(f'/books/{book_id}')

def add_book_for_author(request, author_id):
    Author.objects.get(id = author_id).books.add(Book.objects.get(id=request.POST['which_book']))

    return redirect(f'/authors/{author_id}')

    


