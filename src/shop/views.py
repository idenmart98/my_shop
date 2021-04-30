from django.shortcuts import render
from .models import Product
from .serializers.product import ProductDetailSerializer, ProductsListSerializer
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
# Create your views here.

class ProductDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()
    lookup_field = 'pk'
    lookup_url_kwarg = 'product_id'

class ProductstListView(ListAPIView):
    serializer_class = ProductsListSerializer
    queryset = Product.objects.all()

