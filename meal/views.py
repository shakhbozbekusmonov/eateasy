from django.shortcuts import render

# Create your views here.
from meal.serializers import ProductSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from meal.models import Product


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
