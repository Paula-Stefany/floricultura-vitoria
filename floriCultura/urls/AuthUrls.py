from django.urls import path
from floriCultura.views.AuthView import cadaster_view

urlpatterns = [
    path('cadaster', cadaster_view, name='cadaster'),
]
