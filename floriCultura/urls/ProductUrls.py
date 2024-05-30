from django.urls import path 
from floriCultura.views.ProductView import about_product_view

urlpatterns = [
    path('about_product', about_product_view, name='about_product'),
]

