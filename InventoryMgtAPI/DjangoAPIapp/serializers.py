from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'title'
        )
        model = Category


# class BookSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = (
#             'id',
#             'title',
#             'category',
#             'price',
#             'stock',
#             'description',
#             'status',
#             'date_created'
#         )
#         model = Book


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'category',
            'price',
            'stock',
            'description',
            'status',
            'date_created'
        )
        model = Product