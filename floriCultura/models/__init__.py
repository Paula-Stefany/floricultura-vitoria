from django.db import models 
from django.contrib.auth.models import User 
from django.db.models.signals import post_save
from django.dispatch import receiver 

COLOR_CHOICE = (
    (1, 'Amarelo'),
    (2, 'Azul'),
    (3, 'Vermelho'),
    (4, 'Branco'),
    (5, 'Preto'),
    (6, 'Rosa'),
    (7, 'Champagne'),
    (8, 'Laranja'),
    (9, 'Colorido'),
    (10, 'Lilás'),
    (11, 'Marrom')
)

from .Address import Address
from .Category import Category
from .Product import Product
from .Stock import Stock
from .Client import Client