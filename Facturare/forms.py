from django import forms
from django.forms import formset_factory
from .models import Factura

class FacturaForm(forms.Form):

    pacient = forms.CharField(
        label='Pacientul:',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nume&Prenume Pacient',
            'rows':1
        })
    )
    pacient_email = forms.CharField(
        label='Email-ul Pacientului:',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'pacient@holaruservices.com',
            'rows':1
        })
    )
    adresa_facturare = forms.CharField(
        label='Adresa de facturare',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '',
            'rows':1
        })
    )
    factura_d = forms.CharField(
        label='Detalii:',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Detalii:',
            'rows':1
        })
    )

class LineItemForm(forms.Form):

    serviciu = forms.CharField(
        label='Serviciu:',
        widget=forms.TextInput(attrs={
            'class': 'form-control input',
            'placeholder': 'Denumire serviciu:'
        })
    )
    descriere = forms.CharField(
        label='Descriere:',
        widget=forms.TextInput(attrs={
            'class': 'form-control input',
            'placeholder': 'Utilizarea în detaliu în detaliu a serviciu:',
            "rows":1
        })
    )
    cantitate = forms.IntegerField(
        label='Cantitatea',
        widget=forms.TextInput(attrs={
            'class': 'form-control input quantity',
            'placeholder': 'Cantitatea:'
        }) #quantity should not be less than one
    )
    valoare_monetara = forms.DecimalField(
        label='Valoare monetară:',
        widget=forms.TextInput(attrs={
            'class': 'form-control input rate',
            'placeholder': 'Valoare'
        })
    )

LineItemFormset = formset_factory(LineItemForm, extra=1)
