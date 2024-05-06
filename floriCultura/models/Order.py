from floriCultura.models import *


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    items = models.ManyToManyField(OrderItem)
    order_date = models.DateTimeField(auto_now_add=True)
    Total_price = models.DecimalField(max_digits=10, decimal_places=2)
    coupon = models.ForeignKey(Coupon, on_delete=models.DO_NOTHING)
    address = models.ForeignKey(Address, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'Pedido {self.id}'
    