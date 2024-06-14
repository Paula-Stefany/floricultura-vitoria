from django.urls import path
from floriCultura.views.ClientView import client_profile_view, edit_client_address_view, edit_client_view


urlpatterns = [
    path('', client_profile_view, name='client_profile'),
    path('edit_address', edit_client_address_view, name='edit_address'),
]
