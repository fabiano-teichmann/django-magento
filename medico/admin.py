from django.contrib import admin
from .models import AmastyAmorderattrOrderAttribute, SalesFlatOrder


class AmastyAmorderattrOrderAttributeAdmin(admin.ModelAdmin):
    save_on_top = True
    search_fields = ['entity_id', 'doctor_authorization', 'order']
    list_display = ('entity_id', 'doctor_authorization', 'order')


class MetaAmastyAmorderattrOrderAttribute:
    model = AmastyAmorderattrOrderAttribute
    admin.site.register(AmastyAmorderattrOrderAttribute, AmastyAmorderattrOrderAttributeAdmin)

class SalesFlatOrderAdmin(admin.ModelAdmin):
    save_on_top = True
    search_fields = ['entity_id','status']
    list_display = ('entity_id','status', 'customer_firstname','customer_lastname')

class MetaSalesFlatOrder:
    model = SalesFlatOrder
    admin.site.register(SalesFlatOrder, SalesFlatOrderAdmin)

