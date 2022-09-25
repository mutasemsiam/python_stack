from django.shortcuts import render, redirect
import random
from django import template
from time import strftime, localtime
    
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'log' not in request.session:
        request.session['log'] = []
        
    return render(request, "index.html")
    
def process(request):
    logs= []
    time = strftime("%b %d, %Y  %I:%M %p", localtime())
    if request.POST['gold_game'] == 'gold_farm':
        request.session['gold_found'] = random.randint(10,20)
        logs.append(f"You entered a farm and earned { request.session['gold_found']} gold ({time})")

    if request.POST['gold_game'] == 'gold_cave':
        request.session['gold_found'] = random.randint(10,20)
        logs.append(f"You entered a cave and earned { request.session['gold_found']} gold ({time})")

    if request.POST['gold_game'] == 'gold_house':
        request.session['gold_found'] = random.randint(10,20)
        logs.append(f"You entered a house and earned { request.session['gold_found']} gold ({time})")

    if request.POST['gold_game'] == 'quest':
        request.session['gold_found'] = random.randint(-50,50)
        if request.session['gold_found']<0:
            logs.append(f"You failed a quest and lost { -request.session['gold_found']} gold ({time})")
        else:
            logs.append(f"You completed a quest and earned { request.session['gold_found']} gold ({time})")
    
    request.session['gold'] += request.session['gold_found']
    request.session['log'] += logs
        
    return redirect('/')

def delete(request):
    del request.session['gold']
    del request.session['log']
    return redirect('/')



