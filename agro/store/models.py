from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    featured = models.BooleanField(default=False)
    recent = models.BooleanField(default=True)
    image = models.ImageField()
    category = models.ForeignKey(
        Category, on_delete=models.RESTRICT, related_name='products')

    def __str__(self):
        return self.name


class Carousel(models.Model):
    image = models.ImageField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Review(models.Model):
    pass


class Order(models.Model):
    pass


class Cart(models.Model):
    pass


class Wishlist(models.Model):
    pass
