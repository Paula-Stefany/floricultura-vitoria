from floriCultura.models import *


class Stock(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Stock'

    def __str__(self):
        return f'{self.product.name}'
