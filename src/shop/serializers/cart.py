from rest_framework import serializers
from shop.models import Cart, CartProduct


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    count = serializers.IntegerField()

    class Meta:
        model = Cart
        fields = '__all__'


class CartSerializer(serializers.Serializer):
    customer = serializers.CharField(max_length=30)
    number = serializers.CharField(max_length=20)
    products = ProductSerializer(many=True)

    class Meta:
        model = Cart
        fields = '__all__'
