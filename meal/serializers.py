from rest_framework import serializers
from meal.models import Product, ProductType, Category
from restaurant.models import Restaurant


class Restaurant(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    restaurant = Restaurant()

    class Meta:
        model = Category
        fields = (
            "id",
            "title",
            "restaurant",
        )


class ProductTypeSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    restaurant = Restaurant()

    class Meta:
        model = ProductType
        fields = (
            "id",
            "title",
            "category",
            "restaurant",
        )


class ProductSerializer(serializers.ModelSerializer):
    product_type = ProductTypeSerializer()

    class Meta:
        model = Product
        fields = ("id", "title", "description", "price", "image", "product_type")
