from unicodedata import category
from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    stock = models.IntegerField()
    # imageUrl = models.ImageField()
    status = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.name