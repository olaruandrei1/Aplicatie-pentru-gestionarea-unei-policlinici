from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class FormInregistrare(UserCreationForm):
    username = forms.CharField(
    label = 'Nume de utilizator :',
    required = True,
    help_text = "Numele de utilizator trebuie să conțină cel puțin 8 caractere!",
    error_messages = {'invalid': 'Numele de utilizator introdus este eronat. Încercați alt nume de utilizator!'},
    widget=forms.TextInput(attrs={'class': 'form-control text-center'})
    )

    email = forms.EmailField(
    label = 'Adresa de email :',
    required = True,
    help_text = "Adresa de email trebuie să fie în următorul format: cineva@domeniu.com",
    widget=forms.TextInput(attrs={'class': 'form-control text-center'})
    )

    password1 = forms.CharField(
    widget=forms.PasswordInput(attrs={'class': 'form-control text-center'}),
    label = 'Parola :',
    required = True,
    help_text = "Parola trebuie sa fie de minim 8 caractere & diferită de numele de utilizator și email!",

    )
    password2 = forms.CharField(
    widget=forms.PasswordInput(attrs={'class': 'form-control text-center'}),
    label = 'Reintroduceți parola :',
    required = True,
    )

    class Meta:#configurarea propriu-zisa a formului
        model = User#atribuindu-se aceste modele Utilizatorului
        fields = ['username', 'email', 'password1', 'password2']#aceste campuri vor fi afisate
