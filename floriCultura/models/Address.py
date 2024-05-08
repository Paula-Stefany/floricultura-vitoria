from floriCultura.models import *


class Address(models.Model):
    state = models.ForeignKey(State, null=True, related_name='state', on_delete=models.SET_NULL)
    city = models.ForeignKey(City, null=True, related_name='city', on_delete=models.SET_NULL)
    neighborhood = models.ForeignKey(Neighborhood, null=True, related_name='neighborhood', on_delete=models.SET_NULL)
    street = models.CharField(null=False, max_length=25)
    number = models.CharField(null=False, max_length=15)
    complement = models.CharField(null=False, max_length=40)
    cep = models.CharField(null=False, max_length=12)
    receiver = models.CharField(null=True, blank=True, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Adresses'

    def __str__(self):
        return f'{self.street}'
    