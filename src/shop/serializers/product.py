from rest_framework import serializers
from shop.models import Product, ProductImage
from .category import  CategoryListSerializers

class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        exclude = ['product']



class ProductDetailSerializer(serializers.ModelSerializer):
    photo = ProductImagesSerializer(many=True)
    category = CategoryListSerializers()
    def update(self, instance, data):
        instance = super(ProductDetailSerializer, self).update(instance, data)
        instance.save()
        return instance
                    
    class Meta:
        model = Product
        exclude = ('id',)


class ProductsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


        

       
   