from django.urls import path
from .views import *

urlpatterns = [
    path('categories', ListCategory.as_view(), name='categories'),
    path('categories/<int:pk>/', DetailedCategory.as_view(), name='category'),

    path('products', ListProduct.as_view(), name='products'),
    path('products/<int:pk>/', DetailedProduct.as_view(), name='product'),
]
