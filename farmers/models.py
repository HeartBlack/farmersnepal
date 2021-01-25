from django.db import models
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session


# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length=255,null=True)
    Phone = models.CharField(max_length=50,null=True)
    location = models.CharField(max_length=250,null=True)
    # vuser = models.OneToOneField(User,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name




class Product(models.Model):
    name = models.CharField(max_length=255,null=True)
    price = models.FloatField(null=True)
    description = models.CharField(max_length=500, null=True)
    models.CharField(max_length=250, null=True)    
    quantity = models.IntegerField(null=True)
    image = models.ImageField(upload_to='products/')
    category = models.CharField(max_length=250, null=True)
    vendor = models.ForeignKey(Vendor,on_delete=models.CASCADE,null=True)
    post_date = models.DateField( auto_now=False, auto_now_add=False,null=True)
    discount = models.IntegerField(blank=True,default=True)
    sales = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    



class Order_item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.FloatField(null=True)
    total_ammount = models.FloatField(null=True)
    
    def __str__(self):
        return self.product.name


class Place_order(models.Model):
    order_by = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=500, null=True,blank=True)
    phone = models.IntegerField(null=True,blank=True)
    email = models.EmailField(null=True,blank=True)

    def __str__(self):
        return self.order_by.username


class Contat_us(models.Model):
    name = models.CharField(max_length=250, null=True)
    email = models.EmailField( max_length=254,null=True,unique=True)
    subject = models.CharField(max_length=256,null=True)
    message = models.TextField(max_length=1000,null=True)

    def __str__(self):
        return self.name


class Subscriber(models.Model):
    email = models.EmailField( max_length=254,null=True, unique=True)

   