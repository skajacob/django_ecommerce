"""ecommerce URL Configuration
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from ecommerce.drf import views

router = routers.DefaultRouter()
router.register(r"api", views.AllProductsViewset, basename="allproducts")
router = routers.DefaultRouter()
router.register(
    r"product/(?P<slug>[^/.]+)",
    views.ProductInventoryViewset,
    basename="products",
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("demo/", include("ecommerce.demo.urls", namespace="demo")),
    path("", include("router.urls")),
]
