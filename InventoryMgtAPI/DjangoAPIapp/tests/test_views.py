from django.test import TestCase, Client
from django.urls import reverse
# from models import Product, Category
# import json


class TestViews(TestCase):


    def setUp(self):
        self.client = Client()
        self.product_url = reverse('products')
        self.category_url = reverse('categories')

    def test_product_list(self):

        response = self.client.get(self.product_url)

        self.assertEquals(response.status_code, 200)


    def test_category_list(self):

        response = self.client.get(self.category_url)

        self.assertEquals(response.status_code, 200)
        



