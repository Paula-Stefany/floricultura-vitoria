from floriCultura.models import *


class Address(models.Model):
    state = models.CharField(null=False, max_length=25)
    city = models.CharField(null=False, max_length=25)
    neighborhood = models.CharField(null=False, max_length=25)
    street = models.CharField(null=False, max_length=25)
    number = models.CharField(null=False, max_length=15)
    complement = models.CharField(null=False, max_length=40)
    cep = models.CharField(null=False, max_length=12)
    receiver = models.CharField(null=True, blank=True, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.street}'