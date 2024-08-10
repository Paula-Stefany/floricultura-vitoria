from floriCultura.models import *


class State(models.Model):
    name = models.CharField(max_length=50, null=False)
    uf = models.CharField(max_length=5, unique=True, null=True)

    def __str__(self) -> str:
        return f'{self.name}'
    