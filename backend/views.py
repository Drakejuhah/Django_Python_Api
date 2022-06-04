
from backend.models import Product
from backend.serializers import ProductSerializer
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.


@api_view(['GET', 'POST'])
def all_products(request):
    if request.method == 'GET':
        Products = Product.objects.all()
        serializedProducts = ProductSerializer(Products, many=True)
        return JsonResponse(serializedProducts.data, safe=False)

    if request.method == 'POST':
        serializedProducts = ProductSerializer(data=request.data)
        if serializedProducts.is_valid():
            serializedProducts.save()
            return Response(serializedProducts.data, status=status.HTTP_201_CREATED)
