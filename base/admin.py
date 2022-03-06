from django.contrib import admin
from .models import Category ,Product,Comments,Cart,Order, ShopInfo

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Comments)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(ShopInfo)
