from django.core.cache import cache
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
# Create your views here.
@api_view(
    ["GET"],
)
def product_list(request):
    cache_kye = "products_list"
    if not cache.get(cache_kye):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        json_response = serializer.data
        cache.set("products_list", json_response, 20)
    
    response_data = cache.get(cache_kye)
    return Response(response_data)