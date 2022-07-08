from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.template.loader import get_template
from django.http import HttpResponse
from django.views import View
from .models import LineItem, Factura
from .forms import LineItemFormset, FacturaForm
import pdb

class FacturareListView(View):
    def get(self, *args, **kwargs):
        facturi = Factura.objects.all()
        context = {
            "facturi":facturi,
        }

        return render(self.request, 'Facturare/PaginaPrincipalaFacturi.html', context)

    def post(self, request):

        factura_ids = request.POST.getlist("facturi_id")
        factura_ids = list(map(int, factura_ids))

        update_status_for_facturi = int(request.POST['status'])
        facturi = Factura.objects.filter(id__in=factura_ids)
        if update_status_for_facturi == 0:
            facturi.update(status=False)
        else:
            facturi.update(status=True)

        return redirect('Facturare-FacturaList')

def adauga_factura(request):

    if request.method == 'GET':
        formset = LineItemFormset(request.GET or None)
        form = FacturaForm(request.GET or None)
    elif request.method == 'POST':
        formset = LineItemFormset(request.POST)
        form = FacturaForm(request.POST)

        if form.is_valid():
            factura = Factura.objects.create(pacient=form.data["pacient"],
                    pacient_email =form.data["pacient_email"],
                    adresa_facturare = form.data["adresa_facturare"],
                    data_emitere=form.data["date"],
                    data_expirare=form.data["due_date"],
                    factura_d=form.data["factura_d"],
                    )
            factura.save()

        if formset.is_valid():
            total = 0
            for form in formset:
                serviciu = form.cleaned_data.get('serviciu')
                descriere = form.cleaned_data.get('descriere')
                cantitate = form.cleaned_data.get('cantitate')
                valoare_monetara = form.cleaned_data.get('valoare_monetara')
                if serviciu and descriere and cantitate and valoare_monetara:
                    amount = float(valoare_monetara)*float(cantitate)
                    total += amount
                    LineItem(pacient=factura,
                            serviciu=serviciu,
                            descriere=descriere,
                            cantitate=cantitate,
                            valoare_monetara=valoare_monetara,
                            amount=amount).save()
            factura.total_amount = total
            factura.save()
            try:
                generate_PDF(request, id=factura.id)
            except Exception as e:
                print(f"Ceva nu a funcționat! Contactați admistratorul utilizând secțiunea ”Contact”, atașând următoarea eroare:{e}")
            return redirect('Facturare-FacturaList')
    context = {
        "title" : "Generator de Facturi",
        "formset": formset,
        "form": form,
    }
    return render(request, 'Facturare/adauga_factura.html', context)


def vizualizare_PDF(request, id=None):
    factura = get_object_or_404(Factura, id=id)
    lineitem = factura.lineitem_set.all()

    context = {
        "company": {
            "name": "Health Olaru Services",
            "address" :"Strada Olărescu numărul 22",
            "phone": "+40773832614",
            "email": "holaruservices@gmail.com",
        },
        "factura_id": factura.id,
        "factura_total": factura.total_amount,
        "pacient": factura.pacient,
        "pacient_email": factura.pacient_email,
        "data_emitere": factura.data_emitere,
        "data_expirare": factura.data_expirare,
        "adresa_facturare": factura.adresa_facturare,
        "factura_d": factura.factura_d,
        "lineitem": lineitem,

    }
    return render(request, 'Facturare/VizualizareFactura.html', context)


def change_status(request):
    return redirect('Facturare-FacturaList')

def view_404(request,  *args, **kwargs):
    return redirect('Facturare-FacturaList')
