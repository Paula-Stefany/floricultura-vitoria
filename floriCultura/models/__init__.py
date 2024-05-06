from django.db import models 
from django.contrib.auth.models import User 
from django.db.models.signals import post_save
from django.dispatch import receiver 



from .Address import Address
from .Category import Category
from .Color import Color
from .Product import Product
from .Stock import Stock
from .Client import Client
from .Rating import Rating
from .Coupon import Coupon
from .OrderItem import OrderItem
from .Order import Order
