from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=300)
    image=models.ImageField(null=True, max_length=100,default='')
    
    def __str__(self):
        return "%s %s"%(self.name,self.id)


class Brand(models.Model):
    name=models.CharField(max_length=300)
    image=models.CharField(max_length=300,default='')

    def __str__(self):
        return  self.name




class Product(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    
    admin=models.ForeignKey(User,on_delete=models.CASCADE)
    name= models.CharField(max_length=300)
    price=models.CharField(max_length=20)
    image=models.ImageField(null=True, max_length=100,default='')
  
    description=models.TextField(null=False,blank=False)
    stock=models.IntegerField()
    discount=models.IntegerField(null=True,blank=True)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-updated','-created']

    def __str__(self):
        return self.name    

'''
class Color(models.Model):
    name=models.CharField(max_length=300,default='')   
    product=models.ForeignKey(Product, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.name

class Size(models.Model):
    name=models.CharField(max_length=300,default='') 
    product=models.ForeignKey(Product, on_delete=models.CASCADE,default='')  

    def __str__(self):
        return self.name  
'''

class Comments(models.Model):
    body=models.TextField()
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.body



class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    count=models.TextField(default='')


class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    count=models.IntegerField(null=False,blank=False)

    def __str__(self):
        return self.count


class ShopInfo(models.Model):
    facebook=models.TextField(default='')
    twitter=models.TextField(default='')
    phone=models.TextField(default='')
    email=models.TextField(default='')

    def __str__(self):
        return self.email


    

    
