from django.contrib import admin
from meal.models import Product, ProductType
from django.contrib.admin.sites import AlreadyRegistered
from django.apps import apps

app_models = apps.get_models()
for model in app_models:
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass
