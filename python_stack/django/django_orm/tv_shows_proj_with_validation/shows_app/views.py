from platform import release
from turtle import title
from django.shortcuts import render,redirect
from .models import Show
from django.contrib import messages



def index(request):
    context = {
        "all_shows": Show.objects.all()
    }

    return render(request, "index.html", context)

def add_show(request):

    return render(request, "add_show.html")

def add_new_show(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
        new_show = Show.objects.create(title = request.POST['title'], network = request.POST['network'], release_date = request.POST['release_date'], desc = request.POST['desc'])
    
    return redirect(f'/shows/{new_show.id}')
    

def display_edit(request, show_id):
    context = {
        "show": Show.objects.get(id=show_id),
    }
    
    return render(request, "edit_show.html", context)
def edit_show(request, show_id):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    c = Show.objects.get(id = show_id)
    if request.POST['title']:
        c.title = request.POST['title']
    if request.POST['network']:
        c.network = request.POST['network']
    if request.POST['release_date']:
        c.release_date = request.POST['release_date']
    if request.POST['desc']:
        c.desc = request.POST['desc']
    c.save()
    return redirect(f'/shows/{show_id}')

def display_show(request, show_id):
    context = {
        "show": Show.objects.get(id=show_id),
    }
    
    return render(request, "display_show.html", context)
    
def delete_show(request, show_id):
    c = Show.objects.get(id = show_id)
    c.delete()
    return redirect('/shows')

def redirect_shows(request):
    
    return redirect('/shows')



