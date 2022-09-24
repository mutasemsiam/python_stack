from multiprocessing import context
from django.shortcuts import render,redirect
import random
from django import template

def index(request):
    request.session['guess'] = random.randint(1,100)
    print(request.session['guess'])
    return render(request, "index.html")

def input(request):
    guess_from_user = int(request.POST['user_guess'])

    if guess_from_user < request.session['guess']:
        y = "Too low!"
        color = "blue"

    elif guess_from_user > request.session['guess']:
        y = "Too high!"
        color = "red"

    elif guess_from_user == request.session['guess']:
        y = "You won!!"
        color = "green"
        
    
    context = {
        "output" : y, 
        "color" : color,
    }
    
    return render(request, "show.html", context)

