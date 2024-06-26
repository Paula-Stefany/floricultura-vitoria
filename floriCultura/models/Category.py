from floriCultura.models import * 

class Category(models.Model):
    
    name = models.CharField(null=False, max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Category'

    def __str__(self):
        return f'{self.name}'
    