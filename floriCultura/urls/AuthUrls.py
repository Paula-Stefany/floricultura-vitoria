from django.urls import path
from floriCultura.views.AuthView import cadaster_view, login_view

urlpatterns = [
    path('cadaster', cadaster_view, name='cadaster'),
    path('login', login_view, name='login'),
]
