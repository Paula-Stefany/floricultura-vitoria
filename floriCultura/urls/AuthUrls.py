from django.urls import path
from floriCultura.views.AuthView import cadaster_view, login_view, recovery_view, password_change_view


urlpatterns = [
    path('cadaster', cadaster_view, name='cadaster'),
    path('login', login_view, name='login'),
    path('recovery', recovery_view, name='recovery'),
    path('change-password/<str:token>', password_change_view, name='change-password'),
]
