from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64, unique=True)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    VAT = [(0.23, '0.23'),
           (0.08, '0.08'),
           (0.05, '0.05'),
           (0, '0'),]

    name = models.CharField(max_length=128)
    description = models.TextField()
    price = models.FloatField()
    vat = models.FloatField(choices=VAT)
    stock = models.PositiveIntegerField()
    categories = models.ManyToManyField(Category)
