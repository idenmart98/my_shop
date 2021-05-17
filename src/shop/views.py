import requests
from datetime import datetime, timedelta, timezone
from django.shortcuts import render
from rest_framework.serializers import Serializer

from .models import Product, Category, Review, Cart, CartProduct, ProductImage
from .serializers.product import ProductDetailSerializer, ProductsListSerializer, ProductImagesSerializer
from .serializers.cart import CartSerializer, CartDateSerializer

from .serializers.category import CategoryListSerializers
from .serializers.review import ReviewCreateSerializer
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.conf import settings


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


class CartCreateView(CreateAPIView):
    serializer_class = CartSerializer

    def create(self, request):
        customer = request.data['customer']
        number = request.data['number']
        products = request.data['products']
        
        print(customer, number, products)

        card = Cart.objects.create(
            costummer = customer,
            number = number,
        )
        card.save()

        for product in products:
            product_created = CartProduct.objects.create(
                product = Product.objects.get(id = product['id']),
                card =  Cart.objects.get(id = card.id),
                count = product["count"]
            )
            product_created.save()
            

        return Response({
            'success': True,
            'data': 'Cart created'},
            status.HTTP_201_CREATED
        )

class ReviewCreateView(CreateAPIView):
    serializer_class = ReviewCreateSerializer
    queryset = Review.objects.all()

    def create(self, request):
        customer_name = request.POST.get('customer_name')
        description = request.POST.get('description')
        res = requests.get(settings.URL+f'{customer_name}\n{description}')
        
        return Response({
            "success": True,
            "data": "Review created"},
            status.HTTP_201_CREATED
        )

@api_view(["GET", "POST"])
def statistics(request):
    cart_product_finished = CartProduct.objects.filter(cart__status='finished')
    cart_product_finished_count = cart_product_finished.values_list(
        'count', flat=True)
    cart_product_finished_count_summ = sum(cart_product_finished_count)

    return Response({"cart_product_finished_count_summ": cart_product_finished_count_summ})


@api_view(["GET", "POST"])
def product_statistics(request):
    if request.method == 'POST':
        serializer = CartDateSerializer(data=request.data)
        if serializer.is_valid():
            cart_finished = Cart.objects.filter(status='finished')
            start_date = serializer.data['start_date']
            end_date = serializer.data['end_date']
            cart_finished.filter(created__range=(start_date, end_date))
            cart_count = cart_finished.values_list('id', flat=True)
            cart_product_counts = CartProduct.objects.filter(cart_id__in=cart_count)
            cart_counts = cart_product_counts.values_list('count', flat=True)
            cart_summ = sum(cart_counts)
            return Response({"count":cart_summ})
    return Response()

