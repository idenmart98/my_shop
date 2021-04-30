from django.urls import path, include
from .views import ProductstListView


app_name = 'shop'

urlpatterns = [
    path('product/', ProductstListView.as_view()),
]