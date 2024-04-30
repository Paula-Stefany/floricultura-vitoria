from floriCultura.models import *


class Product(models.Model):
    name = models.CharField(null=False, max_length=30)
    description = models.CharField(null=True, max_length=50, blank=True)
    about = models.CharField(null=True, max_length=150, blank=True)
    care = models.CharField(null=True, max_length=150, blank=True)
    category = models.ForeignKey(Category, related_name='product_category', on_delete=models.CASCADE)
    color = models.IntegerField(choices=COLOR_CHOICE, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    disponibility = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'
