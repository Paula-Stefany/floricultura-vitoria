from floriCultura.models import *
from django.core.validators import MaxValueValidator, MinValueValidator


class Rating(models.Model):

    user = models.ForeignKey(Client, related_name='avaliador', on_delete=models.CASCADE)
    product_rated = models.ForeignKey(Product, related_name='produto_avaliado', on_delete=models.CASCADE)
    value = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Avaliador: {self.user}, Produto avaliado: {self.product_rated}'
    