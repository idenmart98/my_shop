from rest_framework import serializers
from shop.models import Product
# Create your views here.

class ProductsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'