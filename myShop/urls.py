from django.urls import path
from . import views

urlpatterns = [
    path("", views.products_list, name="hello"),
    path("categories/", views.categories_list, name="categories"),
    path("products/", views.products_list, name="products"),
    path("categories/<int:category_id>/products/", views.category_products, name="category_products")
]