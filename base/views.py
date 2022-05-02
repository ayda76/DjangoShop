from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login,logout
from django.contrib.auth.forms import UserCreationForm 
from .models import Product ,Category , Comments,Cart,Order,ShopInfo
from django.contrib.auth.models import User
from django.db.models import Q
# Create your views here.

def home(request):
    q= request.GET.get('q') if request.GET.get('q') !=None else ''
    #__icontains =means that the word has those chars
    products=Product.objects.filter(Q(category__name__icontains=q)| Q(name__icontains=q)| Q(description__icontains=q))
   

    categorys=Category.objects.all()
    shopinfo=ShopInfo.objects.all()
    #products=Product.objects.all()
    #
    woman=Category.objects.get(name='Women')
    
    women=Product.objects.filter(Q(category=woman.id))
    man=Category.objects.get(name='Men')
    
    men=Product.objects.filter(Q(category=man.id))
            

        
    context={'categorys':categorys,'shopinfo':shopinfo, 'products':products,'women':women,'men':men}
    return render(request,'base/home.html',context)

def category(request,pk):
    categorys=Category.objects.get(id=pk)
    context={'categorys':categorys}
    return render(request,context)

def loginUser(request):
    form=UserCreationForm()

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


    return render(request,'base/login.html' ,{'form':form})



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

def product(request,pk):
    categorys=Category.objects.all()
    product=Product.objects.get(id=pk)
    products=Product.objects.filter(Q(category=product.category))
    comments=Comments.objects.filter(Q(product=pk))
    countComment=comments.count()
    context={'product':product, 'comments':comments,'countComment':countComment,'products':products,'categorys':categorys}
    return render(request,'base/product.html',context)    

def shop(request):
    #products=Product.objects.all()
    categorys=Category.objects.all()
    q=request.GET.get('q')
   

    if q==None:
        products=Product.objects.all()
        context={'categorys':categorys,'products':products}
        return render(request,'base/shop.html',context)
    else:
        products=Product.objects.filter(Q(category__name=q)) 
        context={'categorys':categorys,'products':products}
        return render(request,'base/shop.html',context)

       

   
        
    
     
@login_required(login_url='loginUser')  
def cart(request,pk):
    cartItems=Cart.objects.filter(Q(user=request.user))

    if pk=='all':
        context={'cartObjs':cartItems}
        return render(request,'base/cart.html',context)

    else:

       
        countProduct=request.POST.get('count')
        product=Product.objects.get(id=pk)
             
        totalpurchase=0
        cart=cartItems.filter(Q(product__id=pk))
        if cart!=None:
            
            countcart=int(cart.count)
            total=countcart*int(cart.product.price)
            totalpurchase+=total
            countcart+=countProduct
            cart.count=str(countcart)
            cart.save()
            return redirect('cart',pk='all') 

        else:

            cartUser=Cart.objects.create( 

                user=request.user ,
                product=product ,
                count=str(countProduct))
                
            items=Cart.objects.filter(Q(user=request.user))
            return redirect('cart',pk='all')
            
                
            '''
            for cart in cartItems:
                countcart=int(cart.count)
                total=countcart*int(cart.product.price)
                totalpurchase+=total


                if cart.product==pk:
                    countcart=int(cart.count)
                    countcart+=countProduct
                    cart.count=str(countcart)
                    cart.save()
                    return redirect('cart',pk='all') 
                
                  
                   
                    Objs=Cart.objects.all()

                    context={'cartObjs':Objs}
                    return render(request,'base/cart.html',context)  
                     '''           
            
            

            

                   

        context={'cartObjs':cartItems, 'total':total,'totalpurchase':totalpurchase}
        return render(request,'base/cart.html',context)  
    context={'cartObjs':cartItems}          
    return render(request,'base/cart.html',context)              

    


def contact(request):
    return render(request,'base/contact.html')
@login_required(login_url='loginUser') 
def checkbill(request):
    return render(request,'base/check-out.html')

def pricefilter(request):
    products=Product.objects.all()
    if request.method=='POST':
        minimum=request.POST.get('min')
        maximum=request.POST.get('max')
        products=Product.objects.filter(Q(int(minimum)<=price) & Q(price<=int(maximum)))
        context={'products':products}
        return redirect('shop',context) 
     

    context={'products':products}
    return render(request,context) 
        
      