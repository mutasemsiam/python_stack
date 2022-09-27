import re
from django.shortcuts import render,redirect
from .models import Dojo,Ninja


def index(request):
    context = {
        "all_the_dojos": Dojo.objects.all()
    }

    return render(request, "index.html", context)

def add(request):
    if request.POST['add'] == 'dojo':
        Dojo.objects.create(name = request.POST['name'], city = request.POST['city'], state = request.POST['state'])
    
    elif request.POST['add'] == 'ninja':
        Ninja.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], dojo = Dojo.objects.get(name=request.POST['which_dojo']))
        
    return redirect('/')

