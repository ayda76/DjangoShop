from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('login/',views.loginUser,name='loginUser'),
    path('logout/',views.logoutUser,name='logoutUser'),
    path('register/',views.registerUser,name='registerUser'),
    path('cart/',views.cart,name='cart'),
    path('shop/',views.shop,name='shop'),
    path('product/',views.product,name='product'),
    path('contact/',views.contact,name='contact'),
    path('shop/',views.shop,name='shop'),
    path('checkbill/',views.checkbill,name='checkbill'),
]
