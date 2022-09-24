from multiprocessing import context
from django.shortcuts import render,redirect
from .models import User
    
def index(request):
    context = {
        "all_the_users": User.objects.all()
    }

    return render(request, "index.html", context)

def output(request):
    first_name_from_form = request.POST['name1']
    last_name_from_form = request.POST['name2']
    email_from_form = request.POST['email']
    age_from_form = int(request.POST['age'])
    User.objects.create(first_name= first_name_from_form, last_name= last_name_from_form, email_address= email_from_form, age= age_from_form)

    return redirect("/")

