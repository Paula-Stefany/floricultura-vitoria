from floriCultura.models import * 


class City(models.Model):
    state = models.ForeignKey(State,null=True,
    related_name='cities', on_delete=models.SET_NULL)
    name = models.CharField(max_length=50, null=False)


    def __str__(self) -> str:
        return f'{self.name}'
    