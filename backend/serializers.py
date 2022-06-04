from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from backend.models import Product


class ProductSerializer (serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'descpription', 'user', 'image', ]
