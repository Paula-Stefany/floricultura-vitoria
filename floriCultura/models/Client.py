from floriCultura.models import *
from django.contrib.auth.hashers import make_password


class Client(models.Model):
    username = models.CharField(null=False, max_length=30)
    email = models.EmailField(null=False, max_length=254)
    cpf = models.IntegerField(null=False)
    password = models.CharField(null=False, max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    token = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    address = models.ForeignKey(Address, null=False, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.username}'
    
    def save(self, *args, **kwargs):
        if not self.pk:
            self.password = make_password(self.password)
        super(Client, self).save(*args, **kwargs)
    