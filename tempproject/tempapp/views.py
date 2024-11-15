from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from tempapp.models import place, meet


# Create your views here.
def index(request):
    object=place.objects.all()
    object1 = meet.objects.all()
    return render(request,"index.html", {'result':object,'result1':object1})



def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        password1=request.POST['password1']
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email Taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save()
                return redirect('login')
        else:
            print('password not matching')
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            messages.info(request,"invalid credentials")
            return redirect('login')

    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return  redirect('/')

def destinations(request):
    return render(request,"services.html")

def contact(request):
    return render(request,"contact.html")
