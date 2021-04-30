from django.shortcuts import render
from .models import Product,Category
from .serializers.product import ProductDetailSerializer, ProductsListSerializer
from .serializers.category import CategoryListSerializers
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

class CategoryListView(ListAPIView):
    serializer_class = CategoryListSerializers
    queryset = Category.objects.all()    

