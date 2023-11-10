from django.db import models
from utils.models import BaseModel


# Create your models here.
class Restaurant(BaseModel):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    image = models.ImageField(upload_to="restaurant_images/", blank=True)
    description = models.TextField(blank=True)
    owner = models.ForeignKey("user.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
