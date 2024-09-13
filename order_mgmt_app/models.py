from django.db import models
from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from rest_framework.routers import DefaultRouter
from django.urls import path,include


class Customer(models.Model):
    name =models.CharField(max_length=50)
    email =models.EmailField(unique=True)
    address =models.TextField()
    # file = models.FileField()


    def __str__(self):
        return self.email


class Product(models.Model):
    name =models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    qty_available = models.IntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    customer =models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at =models.DateTimeField(auto_now_add=True)
    total_price =models.DecimalField(max_digits=10,decimal_places=2,default=0)


    def calculate_total(self):
        total =sum([item.quantity *item.product.price for item in self.items.all()])
        self.total_price = total
        self.save()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product =models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()


    def save(self, *args, **kwargs):

        if self.quantity > self.product.qty_available:
            raise ValueError('Quantity requested exceeds available stock.')
        super().save(*args, **kwargs)
        self.product.qty_available -=self.quantity
        self.product.save()