from django.urls import path, include
from meal.views import ProductListView

urlpatterns = [
    path(
        "",
        ProductListView.as_view(),
    )
]
