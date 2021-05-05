import requests
from django.shortcuts import render
from .models import Product, Category, Review, Card, CardProduct
from .serializers.product import ProductDetailSerializer, ProductsListSerializer
from .serializers.category import CategoryListSerializers
from .serializers.review import ReviewCreateSerializer
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
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


class ReviewCreateView(CreateAPIView):
    serializer_class = ReviewCreateSerializer
    queryset = Review.objects.all()

    def create(self, request):
        customer_name = request.POST.get('customer_name')
        description = request.POST.get('description')
        res = requests.get(settings.URL+f'{customer_name}\n{description}')
        return Response(res)


@api_view(["GET", "POST"])
def statistics(request):
    cardproduct_finished = CardProduct.objects.filter(card__status='finished')
    cardproduct_finished_count = cardproduct_finished.values_list(
        'count', flat=True)
    cardproduct_finished_count_summ = sum(cardproduct_finished_count)

    return Response({"cardproduct_finished_count_summ": cardproduct_finished_count_summ})
