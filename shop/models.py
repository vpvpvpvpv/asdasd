from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    price = models.PositiveIntegerField()
    count = models.PositiveIntegerField()
    image = models.ImageField(upload_to='images/')
    rating = models.PositiveSmallIntegerField()
    discount = models.PositiveSmallIntegerField()

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    address = models.TextField()
    number = models.CharField(max_length=30)
    email = models.TextField()
    comment = models.TextField()
    count = models.PositiveIntegerField()

