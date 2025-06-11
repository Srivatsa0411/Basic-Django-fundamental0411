from django.db import models


class Offer(models.Model):
    discount_code = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    discount = models.FloatField()

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)