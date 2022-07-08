from django import forms
from .views import Pacient, Fise_Prezentare, Fise_Internari
import datetime

class FormAdaugarePacient(forms.ModelForm):

    numeprenumepacient = forms.CharField(
    label = 'Nume & Prenumele pacientului',
    required = True,
    error_messages = {'invalid': 'Numele & prenumele introduse au un format eronat!'},
    widget=forms.TextInput(attrs={'class': 'form-control text-center bg-dark  border-0 rounded text-light', 'placeholder':'Nume & Prenume '})
    )

    CNP_Pacient  = forms.IntegerField(
    label = 'Codul numeric personal:',
    required = True,
    error_messages = {'invalid': 'CNP-ul introdus are un format eronat!'},
    widget=forms.TextInput(attrs={'class': 'form-control text-center bg-dark  border-0 rounded text-light', 'placeholder':'CNP'})
    )

    telefon_Pacient = forms.IntegerField(
    label = 'Numărul de telefon al pacientului:',
    required = True,
    error_messages = {'invalid': 'Numărul de telefon introdus are un format eronat!'},
    widget=forms.TextInput(attrs={'class': 'form-control text-center bg-dark  border-0 rounded text-light', 'placeholder':'Telefon'})
    )

    emailPacient = forms.EmailField(
    label = 'Adresa de email:',
    required = True,
    error_messages = {'invalid': 'Email-ul introdus are un format eronat!'},
    widget=forms.TextInput(attrs={'class': 'form-control text-center bg-dark border-0 rounded text-light' , 'placeholder':'Email'})
    )

    varsta_Pacient = forms.IntegerField(
    label = 'Vârsta pacientului:',
    required = True,
    error_messages = {'invalid': 'Valoarea vârstei introduse are un format eronat!'},
    widget=forms.TextInput(attrs={'class': 'form-control text-center bg-dark  border-0 rounded text-light', 'placeholder':'Vârstă'})
    )

    Sex = (
        ('M', 'M'),
        ('F', 'F'),
        ('A', 'Altul'),
    )

    optiune_gen = forms.CharField(
    label = 'Sex:',
    required = True,
    error_messages = {'invalid': 'Genul introdus are un format eronat!'},
    widget=forms.Select(choices = Sex, attrs={'class': 'form-control text-center bg-dark  border-0 rounded text-light', 'placeholder':'Sex'})
    )

    adresa_Pacient = forms.CharField(
    label = 'Adresa pacientului:',
    required = True,
    error_messages = {'invalid': 'Adresa introdusă are un format eronat!'},
    widget=forms.TextInput(attrs={'class': 'form-control text-center bg-dark  border-0 rounded text-light', 'placeholder':'Adresa'})
    )

    sedere = (
        ('RO', 'Română'),
        ('CE', 'Cetățean european'),
        ('PS', 'Permis de ședere'),
        ('NS', 'nespecificat'),
    )

    tip_cetatenie = forms.CharField(
    label = 'Tip de ședere:',
    required = True,
    error_messages = {'invalid': 'Tipul de cetățenie introdus are un format eronat!'},
    widget=forms.Select(choices = sedere, attrs={'class': 'form-control text-center bg-dark  border-0 rounded text-light', 'placeholder':'Tip ședere'})
    )

    class Meta:#configurarea propriu-zisa a formului
        model = Pacient#atribuindu-se aceste modele Utilizatorului
        fields = ['numeprenumepacient', 'CNP_Pacient', 'telefon_Pacient', 'emailPacient', 'varsta_Pacient' ,'optiune_gen','adresa_Pacient', 'tip_cetatenie']#aceste campuri vor fi afisate


class FormAdaugaFisaPrezentare(forms.ModelForm):

    CNP_Pacient  = forms.IntegerField(
    label = 'Codul numeric personal:',
    required = True,
    error_messages = {'invalid': 'CNP-ul introdus are un format eronat!'},
    widget=forms.TextInput(attrs={'class': 'form-control text-center bg-dark  border-0 rounded text-light', 'placeholder':'CNP'})
    )

    simptome_initiale = forms.CharField(
    label = 'Simptomele inițiale:',
    required = True,
    error_messages = {'invalid': 'Simptomele introduse au un format eronat!'},
    widget=forms.TextInput(attrs={'class': 'form-control text-center bg-dark  border-0 rounded text-light', 'placeholder':'Simptomele inițiale:'})
    )

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

    optiune_specialitate = forms.CharField(
    label = 'Specialitatea:',
    required = True,
    error_messages = {'invalid': 'Specialitatea introdusă are un format eronat!'},
    widget=forms.Select(choices = Specialitate, attrs={'class': 'form-control text-center bg-dark  border-0 rounded text-light', 'placeholder':'Specialitate:'})
    )

    concluzie_Consult = forms.CharField(
    label = 'Concluzie/Epicriză consult:',
    required = True,
    error_messages = {'invalid': 'concluzia introdusă are un format eronat!'},
    widget=forms.TextInput(attrs={'class': 'form-control text-center bg-dark  border-0 rounded text-light', 'placeholder':'Concluzie consult:'})
    )

    Decizie = (
    ('CA','Consult & Ambulator'),
    ('CI','Consult & Internare de Zi'),
    ('IN','Internare'),
    ('TR','Tratament'),
    ('CZ','Cerere analize'),
    )


    optiune_Decizie = forms.CharField(
    label = 'Decizie finală:',
    required = True,
    error_messages = {'invalid': 'Decizia introdusă are un format eronat!'},
    widget=forms.Select(choices = Decizie, attrs={'class': 'form-control text-center bg-dark  border-0 rounded text-light', 'placeholder':'Decizie:'})
    )

    Plata = (
    ('AC','Asigurare CNAS'),
    ('DD','Decontare directă'),
    ('PT','Parteneriat*'),
    ('PF','Persoană fizică'),
    ('SP','Scutit plată'),
    )

    optiune_plata = forms.CharField(
    label = 'Tip Plată:',
    required = True,
    error_messages = {'invalid': 'Tipul de plată introdus are un format eronat!'},
    widget=forms.Select(choices = Plata, attrs={'class': 'form-control text-center bg-dark  border-0 rounded text-light', 'placeholder':'Tip plată:'})
    )
    Pacient = forms.IntegerField(
    label = 'ID pacient: ',
    required = True,
    error_messages = {'invalid': 'ID-ul introdus are un format eronat!'},
    widget=forms.TextInput(attrs={'class': 'form-control text-center bg-dark border-0 rounded text-light', 'placeholder':'ID Pacient:'})
    )

    class Meta:
        model = Fise_Prezentare
        fields = ['CNP_Pacient','simptome_initiale', 'optiune_specialitate', 'concluzie_Consult', 'optiune_Decizie', 'optiune_plata', 'pacient']


class FormAdaugaFisaInternare(forms.ModelForm):

    CNP_Pacient  = forms.IntegerField(
    label = 'Codul numeric personal:',
    required = True,
    error_messages = {'invalid': 'CNP-ul introdus are un format eronat!'},
    widget=forms.TextInput(attrs={'class': 'form-control text-center bg-dark  border-0 rounded text-light', 'placeholder':'CNP'})
    )

    diagnostic_int_initial  = forms.CharField(
    label = 'Diagnostic inițial:',
    required = True,
    error_messages = {'invalid': 'Diagnosticul introdus are un format eronat!'},
    widget=forms.TextInput(attrs={'class': 'form-control text-center bg-dark  border-0 rounded text-light', 'placeholder':'Diagnostic inițial:'})
    )

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

    sectie_internare = forms.CharField(
    label = 'Selectează secția:',
    required = True,
    error_messages = {'invalid': 'Secția introdusă are un format eronat!'},
    widget=forms.Select(choices = Sectie, attrs={'class': 'form-control text-center bg-dark  border-0 rounded text-light', 'placeholder':'Selectează secția:'})
    )

    Epicriza_internare = forms.CharField(
    label = 'Epicriză :',
    required = True,
    error_messages = {'invalid': 'Epicriza introdusă are un format eronat!'},
    widget=forms.TextInput(attrs={'class': 'form-control text-center bg-dark  border-0 rounded text-light', 'placeholder':'Epicriză :'})
    )

    Data_externare_internare = forms.DateField(
    initial = datetime.date.today,
    label = 'Data maximă de externare :',
    required = True,
    error_messages = {'invalid': 'Data introdusă are un format eronat!'},
    )

    Pacient = forms.IntegerField(
    label = 'ID :',
    required = True,
    error_messages = {'invalid': 'Epicriza introdusă are un format eronat!'},
    widget=forms.TextInput(attrs={'class': 'form-control text-center bg-dark disable border-0 rounded text-light', 'placeholder':'ID Pacient :'})
    )
    class Meta:
        model = Fise_Internari
        fields = ['CNP_Pacient','diagnostic_int_initial', 'sectie_internare', 'Epicriza_internare', 'Data_externare_internare', 'pacient','Pacient']
