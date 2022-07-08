from django.contrib import admin
from Gestiune.models import *

class PacientAdmin(admin.ModelAdmin):
    list_display =['numeprenumepacient', 'CNP_Pacient', 'telefon_Pacient', 'emailPacient', 'optiune_gen','varsta_Pacient','adresa_Pacient','tip_cetatenie','created_at','autor']
    search_fields = ['numeprenumepacient', 'CNP_Pacient', 'tip_cetatenie', 'created_at', 'autor']
    list_filter = ['CNP_Pacient']
    list_per_page = 10

admin.site.register(Pacient, PacientAdmin)

class Fise_PrezentareAdmin(admin.ModelAdmin):
    list_display =['pacient', 'CNP_Pacient', 'simptome_initiale', 'optiune_specialitate', 'concluzie_Consult','optiune_Decizie','optiune_plata','created_at']
    search_fields = ['numeprenumepacient', 'CNP_Pacient', 'optiune_specialitate', 'created_at', 'optiune_Decizie']
    list_filter = ['CNP_Pacient']
    list_per_page = 10

admin.site.register(Fise_Prezentare, Fise_PrezentareAdmin)

class Fise_InternariAdmin(admin.ModelAdmin):
    list_display =['pacient', 'CNP_Pacient', 'created_at', 'Data_externare_internare', 'sectie_internare','diagnostic_int_initial','Epicriza_internare']
    search_fields = ['pacient', 'CNP_Pacient', 'created_at', 'Data_externare_internare', 'sectie_internare']
    list_filter = ['CNP_Pacient']
    list_per_page = 10

admin.site.register(Fise_Internari, Fise_InternariAdmin)
