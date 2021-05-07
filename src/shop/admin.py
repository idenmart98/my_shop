from django.contrib import admin
from .models import Product,ProductImage, Category, Cart,  CartProduct



class ProductImageAdmin(admin.StackedInline):
    model = ProductImage
 
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
 
    class Meta:
       model = Product
 
admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(CartProduct)

