from django.contrib import admin
from Facturare.models import *

class FacturaAdmin(admin.ModelAdmin):
    list_display =['pacient', 'pacient_email', 'adresa_facturare', 'data_emitere', 'data_expirare','factura_d','total_amount','status']
    search_fields = ['pacient', 'pacient_email', 'data_emitere', 'data_expirare']
    list_filter = ['pacient']
    list_per_page = 10

admin.site.register(Factura, FacturaAdmin)

class LineItemAmin(admin.ModelAdmin):
    list_display =['pacient', 'serviciu', 'descriere', 'cantitate', 'valoare_monetara','amount']
    search_fields = ['pacient', 'serviciu', 'cantitate', 'valoare_monetara']
    list_filter = ['pacient']
    list_per_page = 10

admin.site.register(LineItem, LineItemAmin)
