from rest_framework import serializers
from shop.models import Card, CardProduct


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    count = serializers.IntegerField()

    class Meta:
        model = Card
        fields = '__all__'


class CartSerializer(serializers.Serializer):
    customer = serializers.CharField(max_length=30)
    number = serializers.CharField(max_length=20)
    products = ProductSerializer(many=True)

    class Meta:
        model = Card
        fields = '__all__'
