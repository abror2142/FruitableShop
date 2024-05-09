import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Country(models.Model):
    country_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    title = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True,
                               on_delete=models.CASCADE, related_name='subcategories')
    image = models.ImageField(upload_to="category/")
    description = models.TextField()
    slug = models.SlugField()

    def __str__(self):
        return self.title


class Quality(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Check(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Certificate(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    certifier = models.CharField(max_length=255)  # Organization Name
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    certified_at = models.DateTimeField(default=now)
    valid_for = models.IntegerField(default=3)  # months

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="products/")
    discount = models.IntegerField(default=0)
    valid_for = models.IntegerField(default=48)  # In hours
    produced_at = models.DateTimeField(default=now)
    country_origin = models.ForeignKey(Country, null=True, blank=True, on_delete=models.SET_NULL)
    manufacturer = models.CharField(max_length=255)
    weight = models.DecimalField(max_digits=10, decimal_places=3)
    stock_quantity = models.IntegerField(default=0)
    slug = models.SlugField()
    quality = models.ManyToManyField(Quality)
    checking = models.ForeignKey(Check, null=True, blank=False, on_delete=models.SET_NULL)
    certificate = models.ForeignKey(Certificate, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Rating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mark = models.IntegerField()

    def __str__(self):
        return f"{self.product} {self.mark}"
