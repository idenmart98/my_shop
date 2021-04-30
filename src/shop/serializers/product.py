from rest_framework import serializers
from shop.models import Product,Category



class ProductDetailSerializer(serializers.ModelSerializer):
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

       
   