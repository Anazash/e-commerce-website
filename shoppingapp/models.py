from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Usermember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=255)
    age = models.IntegerField()
    number = models.CharField(max_length=255)
    

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=255, default='default value')
    description=models.CharField(max_length=255)
    price=models.IntegerField(default=0)
    image=models.ImageField(blank=True,upload_to="image/", null=True)
    

class Cart(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    quantity = models.IntegerField(default=1)

   