from floriCultura.models import *


class Color(models.Model):
    name = models.CharField(max_length=50)
    color_code = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'    