from django.urls import path, include
from .views import ProductDetailView

app_name = 'shop'

urlpatterns = [
    path('product/<int:product_id>', ProductDetailView.as_view())
]