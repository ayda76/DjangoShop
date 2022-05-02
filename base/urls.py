from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.home,name='home'),
    path('login/',views.loginUser,name='loginUser'),
    path('logout/',views.logoutUser,name='logoutUser'),
    path('register/',views.registerUser,name='registerUser'),
    path('cart/<str:pk>',views.cart,name='cart'),
    path('shop/',views.shop,name='shop'),
    path('product/<str:pk>',views.product,name='product'),
    path('contact/',views.contact,name='contact'),
    path('checkbill/',views.checkbill,name='checkbill'),
    path('category/<str:pk>',views.category,name='category'),
    path('pricefilter/',views.pricefilter,name='pricefilter'),
    
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)