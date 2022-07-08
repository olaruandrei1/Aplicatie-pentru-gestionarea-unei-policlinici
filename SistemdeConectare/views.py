from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FormInregistrare

def Despre(request):
    return render(request, 'SistemdeConectare/Despre.html')

def Conectare(request):
    return render(request, 'SistemdeConectare/Conectare.html')

def Inregistrare(request):
    if request.method == 'POST':
        form = FormInregistrare(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Contul a fost creat cu success, {username}!')
            return redirect('Gestiune-PaginadeStart')
    else:
        form= FormInregistrare()
    return render(request, 'SistemdeConectare/Inregistrare.html', {'form':form})
