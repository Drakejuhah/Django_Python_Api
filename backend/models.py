from email.mime import image
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    descpription = models.TextField()
    image = models.FileField(upload_to='resources/product')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
