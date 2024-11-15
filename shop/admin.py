from django.contrib import admin
from .models import Product, Order


# Register your models here.  
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(Order)
class OrderAdmin (admin.ModelAdmin):
    pass