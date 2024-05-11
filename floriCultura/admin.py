from django.contrib import admin
from .models import *

class ClientAdmin(admin.ModelAdmin):

    date_hierarchy = 'created_at'
    list_display = ('username', 'created_at', 'address_list')
    list_display_links = ('username', 'address_list')
    empty_value_display = 'Vazio'
    exclude = ('token',)
    search_fields = ('username',)
    list_filter = ('username',)


    fieldsets = (
        ('Dados Pessoais', {
            'fields': ('username', 'email', 'cpf', 'password', 'image')
        }),
        ('Endereço do Entrega', {
            'fields': ('address',)
        }),
    )

    def address_list(self, obj):
        if obj.address:
            return f'{obj.address.city} - {obj.address.state}'


admin.site.register(Client, ClientAdmin)
admin.site.register(Address)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Stock)
admin.site.register(Coupon)
admin.site.register(Color)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Rating)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Neighborhood)
