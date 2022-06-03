from django.shortcuts import render
from rest_framework import generics
from rest_framework import filters
from .serializers import *
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.


# class SuperUserRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):

#     def test_func(self):
#         return self.request.user.is_superuser


class ListCategory(LoginRequiredMixin, generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class DetailedCategory(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
        queryset = Category.objects.all()
        serializer_class = CategorySerializer


class ListProduct(LoginRequiredMixin, generics.ListCreateAPIView):
    queryset = Product.objects.all()
    search_fields = ['description']
    filter_backends = (filters.SearchFilter,)
    serializer_class = ProductSerializer


class DetailedProduct(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


