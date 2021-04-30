from django.contrib import admin
from .models import Product,Image

# Register your models here.

admin.site.register(Product)

class ImageInline(admin.TabularInline):
    fk_name = 'product'
    model = Image

class TrouserAdmin(admin.ModelAdmin):
    inlines = [ImageInline,]