from rest_framework import serializers
from shop.models import Product



class ProductDetailSerializer(serializers.ModelSerializer):
    def update(self, instance, data):
        instance = super(Product_detailsListSerializers, self).update(instance, data)
        instance.save()
        return instance
                    
    class Meta:
        model = Product
        exclude = ('id',)