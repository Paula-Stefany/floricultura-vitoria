from django.contrib import admin
from .models import *
from django.contrib.auth import get_user_model



class ClientAdmin(admin.ModelAdmin):

    date_hierarchy = 'created_at'
    list_display = ('created_at', 'address_list', 'usernames_list')
    list_display_links = ('address_list', 'usernames_list')
    empty_value_display = 'Vazio'
    exclude = ('token',)


    fieldsets = (
        ('Dados Pessoais', {
            'fields': ( 'cpf', 'image')
        }),
        ('Endereço do Entrega', {
            'fields': ('address',)
        }),
    )

    def address_list(self, obj):
        if obj.address:
            return f'{obj.address.city} - {obj.address.city.state}'
    
    def usernames_list(self, obj):
        if obj.user:
            return f'{obj.user.username}'


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
