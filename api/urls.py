from django.urls import path
from .views import *

urlpatterns = [

    path('products/', CreateProductView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]

