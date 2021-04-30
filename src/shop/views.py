from django.shortcuts import render
from .models import Product
from .serializers.product import ProductDetailSerializer, ProductsListSerializer
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

class ProductDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()
    lookup_field = 'pk'
    lookup_url_kwarg = 'product_id'

class ProductstListView(ListAPIView):
    serializer_class = ProductsListSerializer
    queryset = Product.objects.all()

@api_view(['GET'])
def category_details(request, category_id):
    products = Product.objects.filter(category__id = category_id)
    print(products)
    if products:
        ser = ProductsListSerializer(products, many = True)
        return Response({'data': ser.data})
    return Response({'data': 'error'})
