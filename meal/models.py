from django.db import models
from utils.models import BaseModel


# Create your models here.
class Category(BaseModel):
    title = models.CharField(max_length=255)

    restaurant = models.ForeignKey("restaurant.Restaurant", on_delete=models.CASCADE)


# Create your models here.
class ProductType(BaseModel):
    title = models.CharField(max_length=255)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    restaurant = models.ForeignKey("restaurant.Restaurant", on_delete=models.CASCADE)


class Product(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.ImageField(upload_to="product_images")

    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    restaurant = models.ForeignKey("restaurant.Restaurant", on_delete=models.CASCADE)
