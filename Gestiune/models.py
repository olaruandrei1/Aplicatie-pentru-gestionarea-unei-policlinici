from django.db import models
from django.utils import timezone
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Pacient(models.Model):
    Sex = (
        ('M', 'M'),
        ('F', 'F'),
        ('A', 'Altul'),
    )
    sedere = (
        ('RO', 'Română'),
        ('CE', 'Cetățean european'),
        ('PS', 'Permis de ședere'),
        ('NS', 'nespecificat'),
    )

    numeprenumepacient = models.CharField(max_length=60)
    CNP_Pacient = models.BigIntegerField()
    telefon_Pacient = models.IntegerField()
    emailPacient = models.CharField(max_length=60)
    optiune_gen = models.CharField(max_length=1, choices=Sex)
    varsta_Pacient = models.IntegerField(default = '1')
    adresa_Pacient = models.CharField(max_length=100)
    tip_cetatenie = models.CharField(choices=sedere, max_length=20)
    created_at = models.DateTimeField(default=timezone.now)
    autor =models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.numeprenumepacient

    def get_absolute_url(self):
        return reverse('Gestiune-PaginaVizualizarePacient', kwargs={'pk': self.pk})


class Fise_Prezentare(models.Model):
    Specialitate = (
    ('NE','Neurologie'),
    ('GS','Gastroenterologie'),
    ('BI','Medicină Internă/Boli Interne'),
    ('ND','Nutriție și Diabet'),
    ('CD','Cardiologie'),
    ('DM','Dermatologie(Venerologie)'),
    ('OC','Oncologie'),
    ('UR','Urologie'),
    ('PD','Pediatrie'),
    ('OF','Oftalmologie'),
    ('OG','Obstetrică Ginecologie'),
    )
    Decizie = (
    ('CA','Consult & Ambulator'),
    ('CI','Consult & Internare de Zi'),
    ('IN','Internare'),
    ('TR','Tratament'),
    ('CZ','Cerere analize'),
    )
    Plata = (
    ('AC','Asigurare CNAS'),
    ('DD','Decontare directă'),
    ('PT','Parteneriat*'),
    ('PF','Persoană fizică'),
    ('SP','Scutit plată'),
    )
    pacient = models.ForeignKey(Pacient, on_delete = models.CASCADE)
    CNP_Pacient = models.BigIntegerField(default='1234567891234')
    simptome_initiale = models.CharField(max_length = 100)
    optiune_specialitate = models.CharField(max_length = 60, choices = Specialitate)
    concluzie_Consult = models.CharField(max_length = 100, null = True)
    optiune_Decizie = models.CharField(max_length = 50, choices = Decizie)
    optiune_plata = models.CharField(max_length = 40, choices = Plata)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Pacient.numeprenumepacient

    def get_absolute_url(self):
        return reverse('Gestiune-PaginaVizualizareFisaPrezentare', kwargs={'pk': self.pk})

class Fise_Internari(models.Model):
    Sectie = (
    ('NE','Neurologie'),
    ('GS','Gastroenterologie'),
    ('BI','Medicină Internă/Boli Interne'),
    ('ND','Nutriție și Diabet'),
    ('CD','Cardiologie'),
    ('DM','Dermatologie(Venerologie)'),
    ('OC','Oncologie'),
    ('UR','Urologie'),
    ('PD','Pediatrie'),
    ('OF','Oftalmologie'),
    ('OG','Obstetrică Ginecologie'),
    )
    pacient = models.ForeignKey(Pacient, on_delete = models.CASCADE)
    CNP_Pacient = models.BigIntegerField(default='1234567891234')
    created_at = models.DateTimeField(auto_now_add=True)
    Data_externare_internare = models.DateField()
    sectie_internare = models.CharField(choices = Sectie, max_length=50)
    diagnostic_int_initial = models.CharField(max_length=100)
    Epicriza_internare = models.CharField(max_length=100, null = True)

    def __str__(self):
        return self.id

    def get_absolute_url(self):
        return reverse('Gestiune-PaginaVizualizareFisaInternare', kwargs={'pk': self.pk})
