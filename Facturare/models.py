from django.db import models
import datetime

class Factura(models.Model):
    pacient = models.CharField(max_length=100)
    pacient_email = models.EmailField(null=True, blank=True)
    adresa_facturare = models.TextField(null=True, blank=True)
    data_emitere = models.DateField()
    data_expirare = models.DateField(null=True, blank=True)
    factura_d = models.TextField(default= "this is a default message.")
    total_amount = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    status = models.BooleanField(default=False)
    def __str__(self):
        return str(self.pacient)

    def get_status(self):
        return self.status

class LineItem(models.Model):
    pacient = models.ForeignKey(Factura, on_delete=models.CASCADE)
    serviciu = models.TextField()
    descriere = models.TextField()
    cantitate = models.IntegerField()
    valoare_monetara = models.DecimalField(max_digits=9, decimal_places=2)
    amount = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return str(self.pacient)
