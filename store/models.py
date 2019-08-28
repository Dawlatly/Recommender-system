from django.db import models
from django import forms
from django.contrib.auth.models import User
from datetime import date
from django.core.validators import MinValueValidator

# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User)
    confirm_password = models.CharField(null=False, max_length=50, default='')
    age = models.IntegerField(default=0)
    address = models.CharField(null=False, default='',max_length=200)
    address2 = models.CharField(null=False, default='', max_length=200)
    city = models.CharField(null=False, default='', max_length=50)
    state = models.CharField(null=False, default='', max_length=50)
    zipcode = models.CharField(null=False, default='',max_length=5)


    def __str__(self):
        return self.user.username

class Category(models.Model):
    category_Name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_Name

class SubCategory(models.Model):
    subcategory_Name = models.CharField(max_length=50)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.subcategory_Name


class Product(models.Model):
    product_Id = models.IntegerField(primary_key=True)
    product_Name = models.CharField(max_length=30)
    product_Description = models.CharField(max_length=200)
    product_Category = models.ForeignKey(Category,on_delete=models.CASCADE)
    product_SubCategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    product_Price = models.DecimalField(decimal_places=2, max_digits=7)

    def __str__(self):
        return self.product_Name

class Order(models.Model):
    order_Id = models.AutoField(primary_key=True)
    order_Customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    order_Date = models.DateField(default=date.today)
    order_Total = models.FloatField(default=0)

    def __str__(self):
        return self.order_Id.__str__()

class OrderProducts(models.Model):
    Id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.order.__str__()

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    cart_Customer = models.OneToOneField(Customer)
    cart_Products = models.ManyToManyField(Product,blank=True)

    def __str__(self):
        return self.id.__str__()