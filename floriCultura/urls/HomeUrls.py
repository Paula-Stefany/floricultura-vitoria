from django.urls import path
from floriCultura.views.HomeView import home_view


urlpatterns = [
    path('floriculturavitoria', home_view, name='floricultura_vitoria'),
    path('floriculturavitoria/<int:category_id>', home_view, name='floricultura_vitoria'),
]
