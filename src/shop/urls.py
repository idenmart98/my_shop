from django.urls import path, include
from .views import ProductDetailView, ProductstListView,CategoryListView

app_name = 'shop'

urlpatterns = [
    path('product/', ProductstListView.as_view()),
    path('product/<int:product_id>', ProductDetailView.as_view()),
    path('category/',CategoryListView.as_view()),
]