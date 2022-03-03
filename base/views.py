from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate , login,logout
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
    return render(request,'base/register.html')
    
def cart(request):
    return render(request,'base/cart.html')