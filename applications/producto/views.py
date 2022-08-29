from django.shortcuts import render
#
from .models import Product
#
from rest_framework.generics import (
    ListAPIView,
)
from .serializers import ProductSerializer

# Create your views here.

class ListProductUser(ListAPIView):
    
    serializer_class = ProductSerializer

    def get_queryset(self):

        return Product.objects.all()