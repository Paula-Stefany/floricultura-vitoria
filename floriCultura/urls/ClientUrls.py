from django.urls import path
from floriCultura.views.ClientView import client_profile_view


urlpatterns = [
    path('', client_profile_view, name='client_profile'),
]
