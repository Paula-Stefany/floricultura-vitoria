from floriCultura.models import *
from django.contrib.auth.hashers import make_password


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role  = models.IntegerField(choices=ROLE_CHOICE, default=2)
    cpf = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    token = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    address = models.ForeignKey(Address, null=False, on_delete=models.PROTECT)
    
    def __str__(self):
        return f'{self.user.username}'
    
    '''@receiver(post_save, sender=User)
    def create_user_client(sender, instance, created, **kwargs):
        try:
            if created:
                Client.objects.create(user=instance)
        except:
            pass'''
    
    @receiver(post_save, sender=User)
    def save_user_client(sender, instance, **kwargs):
        try:
            instance.client.save()
        except:
            pass
    