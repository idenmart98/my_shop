from django.shortcuts import render
from .models import Product
from .serializers.product import ProductDetailSerializer, ProductsListSerializer
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

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
