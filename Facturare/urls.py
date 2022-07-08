from django.contrib import admin
from django.urls import path
from .views import *
from Facturare.views import *
from Facturare.urls import *

urlpatterns = [
    path('FacturaList', FacturareListView.as_view(), name="Facturare-FacturaList"),
    path('adauga_factura/', adauga_factura, name="Facturare-adauga_factura"),
    path('Factura-detail/<id>', vizualizare_PDF, name='Facturare-FacturaDetail'),
]
