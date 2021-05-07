from django.shortcuts import render
from .models import Product, Category, CardProduct, Card
from .serializers.product import ProductDetailSerializer, ProductsListSerializer
from .serializers.cart import CartSerializer
from .serializers.category import CategoryListSerializers
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


class ProductDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()
    lookup_field = 'pk'
    lookup_url_kwarg = 'product_id'


class ProductstListView(ListAPIView):
    serializer_class = ProductsListSerializer
    queryset = Product.objects.all()


class CategoryDetailView(ListAPIView):
    serializer_class = ProductsListSerializer

    def get_queryset(self):
        return Product.objects.filter(category__id=self.kwargs['category_id'])


class CategoryListView(ListAPIView):
    serializer_class = CategoryListSerializers
    queryset = Category.objects.all()

# @api_view(['GET'])
# def cart_create(request):
    # ser = CartSerializer(data = request.data)
    # ser.is_valid(raise_exception = True)
    # card = Card.objects.create(
    #     custommer = ser.data['custommer'],
    #     number = ser.data['number'],
    #     card_product = ser.data['card_product']
    # )
#     return card


class CartCreateView(CreateAPIView):
    serializer_class = CartSerializer

    def create(self, request):
        customer = request.data['customer']
        number = request.data['number']
        products = request.data['products']
        
        print(customer, number, products)

        card = Card.objects.create(
            costummer = customer,
            number = number,
        )
        card.save()

        for product in products:
            product_created = CardProduct.objects.create(
                product = Product.objects.get(id = product['id']),
                card =  Card.objects.get(id = card.id),
                count = product["count"]
            )
            product_created.save()
            

        return Response({
            'success': True,
            'data': 'Cart created'},
            status.HTTP_201_CREATED
        )
