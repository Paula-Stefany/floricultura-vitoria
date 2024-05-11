from django.urls import path
from floriCultura.views.HomeView import home_view


urlpatterns = [
    path('', home_view),
]
