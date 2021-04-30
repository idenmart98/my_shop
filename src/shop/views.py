from django.shortcuts import render
from django.http import JsonResponse
from .models import Product
from .serializers.product import ProductDetailSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
# Create your views here.


class ProductDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()
    lookup_field = 'pk'
    lookup_url_kwarg = 'product_id'