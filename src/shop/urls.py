from django.urls import path, include
from .views import ProductstListView


app_name = 'shop'

urlpatterns = [
    path('all_products/', ProductstListView.as_view()),
]