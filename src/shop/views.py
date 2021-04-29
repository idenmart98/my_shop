from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Product
from rest_framework.generics import ListAPIView
from .serializers.products import ProductsListSerializer
# Create your views here.

class ProductstListView(ListAPIView):
    serializer_class = ProductsListSerializer
    queryset = Product.objects.all()
