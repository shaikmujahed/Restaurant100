from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import RedirectView
from django.contrib import messages
from django.views import generic

from .forms import CreateUserForm
from .models import *


# Create your views here.
@login_required(login_url='loginPage')
def home(request):
    """View function for home page of site."""
    return render(request, 'index.html')

@login_required(login_url='loginPage')
def BookTable(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        date = request.POST['date']
        time = request.POST['time']
        people = request.POST['people']
        message = request.POST['message']
        instances = BookaTable(name=name, email=email, phone=phone, 
                                Date=date, Time=time, number_of_people=people,
                                 message=message)
        instances.save()
        print('Booking confirm')
    return render(request,'index.html')


@login_required(login_url='loginPage')
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        isinstances = Contact(name=name, email=email,
                                subject=subject, message=message)
        
        isinstances.save()
    #context = {'contact_data':contact_data}
    return render(request,'index.html')
    
def RegisterPage(request):
    if request.user.is_authenticated:
        return redirect('HomeViwe')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('loginPage')

        context = {'form':form}
        return render(request, 'registration.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('HomeViwe')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('HomeViwe')
            else:
                messages.info(request, 'Username or Password is Incorrect')
        context = {}    
        return render(request, 'login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('loginPage')





    

