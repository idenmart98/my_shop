from django.urls import path, include
from .views import ProductDetailView, ProductstListView, CategoryDetailView, CategoryListView, ReviewCreateView,cardproducts_finished

app_name = 'shop'

urlpatterns = [
    path('product/', ProductstListView.as_view()),
    path('product/<int:product_id>', ProductDetailView.as_view()),
    path('category/',CategoryListView.as_view()),
    path('category/<int:category_id>', CategoryDetailView.as_view()),
    path('create/review', ReviewCreateView.as_view()),
    path('cardproducts_finished/',cardproducts_finished)
]