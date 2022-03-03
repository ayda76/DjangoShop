from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate , login,logout
from django.contrib.auth.forms import UserCreationForm 
from .models import Product ,Category , Comments,Cart,Order
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    return render(request,'base/home.html')


def loginUser(request):

    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method== 'POST': 
        username=request.POST.get('username').lower()
        password=request.POST.get('password')
        try:
            user=User.objects.get(username=username)
        
        except:
            messages.error(request,'user does not exist')

            
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')


    return render(request,'base/login.html')



def logoutUser(request,):
    logout(request)
    return redirect('home')

def registerUser(request):

    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'an error occurred')

    return render(request,'base/register.html',{'form':form})

def product(request):
    return render(request,'base/product.html')    

def shop(request):
    return render(request,'base/shop.html')    
    
def cart(request):
    return render(request,'base/cart.html')

def contact(request):
    return render(request,'base/contact.html')

def checkbill(request):
    return render(request,'base/check-out.html')