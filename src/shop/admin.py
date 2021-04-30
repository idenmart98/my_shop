from django.contrib import admin
from .models import Product,ProductImage


admin.site.register(ProductImage)
admin.site.register(Product)

class ProductImageAdmin(admin.StackedInline):
    model = ProductImage
 

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
 
    class Meta:
       model = Product
 
