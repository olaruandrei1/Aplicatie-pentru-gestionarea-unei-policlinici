from urllib import request
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
from Gestiune.models import Pacient, Fise_Prezentare, Fise_Internari
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . import forms, models
from django.contrib.auth.mixins import LoginRequiredMixin


def PaginadeStart(request):
    return render(request, 'Gestiune/PaginadeStart.html')

@login_required
def Contact(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['messages']

        send_mail(subject,
        message,
        settings.EMAIL_HOST_USER,
        ['holaruservices@gmail.com'],
        fail_silently = False
        )
    return render(request, 'Gestiune/Contact.html')

@login_required
def getPacienti(request):
    context = {
        'pacienti': Pacient.objects.all()
    }
    return render(request, 'Gestiune/PaginaPrincipala.html', context)
context = {
    'prezentari': Fise_Prezentare.objects.all()
}
@login_required
def getPrezentari(request):
    context = {
        'prezentari': Fise_Prezentare.objects.all()
    }
    return render(request, 'Gestiune/PaginaOpis.html', context)

@login_required
def getInternari(request):
    context = {
        'internari': Fise_Internari.objects.all()
    }
    return render(request, 'Gestiune/PaginaOpisInternari.html', context)

class PacientiListView(LoginRequiredMixin, ListView):
    model = Pacient
    template_name = 'Gestiune/PaginaPrincipala.html'
    context_object_name ='pacienti'
    ordering = ['-created_at']
    paginate_by = 10
    
    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        query = self.request.GET.get('q')
        if query:
            return qs.filter(Q(CNP_Pacient__icontains = query)|Q(numeprenumepacient__icontains = query)|Q(telefon_Pacient__icontains = query)|Q(emailPacient__icontains = query)|Q(optiune_gen__icontains = query)|Q(varsta_Pacient__icontains = query)|Q(tip_cetatenie__icontains = query))   
        else:
            return Pacient.objects.all()
        
    
class PacientiDetailView(LoginRequiredMixin, DetailView):
    model = Pacient
    template_name = 'Gestiune/PaginaVizualizarePacient.html'
    context_object_name = 'pacienti'
    paginate_by = 3

    def get_context_data(self,*args, **kwargs):
        context = super(PacientiDetailView, self).get_context_data(*args,**kwargs)
        context['prezentari'] = Fise_Prezentare.objects.filter(pacient_id=self.request.resolver_match.kwargs['pk'])
        context['internari'] = Fise_Internari.objects.filter(pacient_id=self.request.resolver_match.kwargs['pk'])
        return context

class PacientiDeleteView(LoginRequiredMixin,  DeleteView):
    model = Pacient
    template_name = 'Gestiune/PaginaStergerePacient.html'
    success_url = '/PaginaPrincipala'

    def form_valid(self, form):
        messages.success(self.request, f"Profil șters cu succes!")
        form.instance.save()
        return super().form_valid(form)

class PacientiCreateView(LoginRequiredMixin, CreateView):
    model = Pacient
    template_name = 'Gestiune/PaginaAdaugarePacient.html'
    form_class = forms.FormAdaugarePacient

    def form_valid(self, form):
        form.instance.autor = self.request.user
        form.instance.save()
        messages.success(self.request, f"Profil creat cu succes!")
        return super().form_valid(form)

class PacientiUpdateView(LoginRequiredMixin,  UpdateView):
    model = Pacient
    template_name = 'Gestiune/PaginaAdaugarePacient.html'
    form_class = forms.FormAdaugarePacient

    def form_valid(self, form):
        form.instance.autor = self.request.user
        form.instance.save()
        messages.success(self.request, f"Profil edidat cu succes!")
        return super().form_valid(form)

class InternareCreateView(LoginRequiredMixin, CreateView):
    model = Fise_Internari
    template_name = 'Gestiune/PaginaAdaugareInternare.html'
    form_class = forms.FormAdaugaFisaInternare

    def form_valid(self, form):
        form.instance.autor = self.request.user
        form.instance.save()
        messages.success(self.request, f"Fișă de internare creată cu succes!")
        return super().form_valid(form)

class InternareUpdateView(LoginRequiredMixin,  UpdateView):
    model = Fise_Internari
    template_name = 'Gestiune/PaginaAdaugareInternare.html'
    form_class = forms.FormAdaugaFisaInternare

    def form_valid(self, form):
        form.instance.autor = self.request.user
        form.instance.save()
        messages.success(self.request, f"Fișă de internare edidată cu succes!")
        return super().form_valid(form)

class InternareDeleteView(LoginRequiredMixin,  DeleteView):
    model = Fise_Internari
    template_name = 'Gestiune/PaginaStergereFisaInternare.html'
    success_url = '/PaginaPrincipala'#

    def form_valid(self, form):
        messages.success(self.request, f"Fișă de internare ștearsă cu succes!")
        return super().form_valid(form)

class InternareListView(LoginRequiredMixin, ListView):
    model = Fise_Internari
    template_name = 'Gestiune/PaginaOpisInternari.html'
    context_object_name ='internari'
    ordering = ['-created_at']
    
    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        query = self.request.GET.get('q')
        
        if query:
            return qs.filter(Q(CNP_Pacient__icontains = query)|Q(Data_externare_internare__icontains = query)|Q(sectie_internare__icontains = query)|Q(diagnostic_int_initial__icontains = query)|Q(Epicriza_internare__icontains = query))   
        else:
            return Fise_Internari.objects.all()

class InternareDetailView(LoginRequiredMixin, DetailView):
    model = Fise_Internari
    template_name = 'Gestiune/PaginaVizualizareFisaInternare.html'

class PrezentariListView(LoginRequiredMixin, ListView):
    model = Fise_Prezentare
    template_name = 'Gestiune/PaginaOpis.html'
    context_object_name ='prezentari'
    ordering = ['-created_at']
    
    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        query = self.request.GET.get('q')
        if query:
            return qs.filter(Q(CNP_Pacient__icontains = query)|Q(simptome_initiale__icontains = query)|Q(optiune_specialitate__icontains = query)|Q(concluzie_Consult__icontains = query)|Q(optiune_Decizie__icontains = query)|Q(optiune_plata__icontains = query))   
        else:
            return Fise_Prezentare.objects.all()

class PrezentareCreateView(LoginRequiredMixin, CreateView):
    model = Fise_Prezentare
    template_name = 'Gestiune/PaginaAdaugaFisaPrezentare.html'
    form_class = forms.FormAdaugaFisaPrezentare

    def form_valid(self, form):
        form.instance.autor = self.request.user
        form.instance.save()
        messages.success(self.request, f"Fișă de prezentare creată cu succes!")
        return super().form_valid(form)

class PrezentareUpdateView(LoginRequiredMixin,  UpdateView):
    model = Fise_Prezentare
    template_name = 'Gestiune/PaginaAdaugaFisaPrezentare.html'
    form_class = forms.FormAdaugaFisaPrezentare

    def form_valid(self, form):
        form.instance.autor = self.request.user
        form.instance.save()
        messages.success(self.request, f"Fișă de prezentare edidată cu succes!")
        return super().form_valid(form)

class PrezentareDeleteView(LoginRequiredMixin,  DeleteView):
    model = Fise_Prezentare
    template_name = 'Gestiune/PaginaStergereFisaPrezentare.html'
    success_url = '/PaginaPrincipala'

    def form_valid(self, form):
        messages.success(self.request, f"Fișă de prezentare ștearsă cu succes!")
        return super().form_valid(form)

class PrezentareDetailView(LoginRequiredMixin, DetailView):
    model = Fise_Prezentare
    template_name = 'Gestiune/PaginaVizualizareFisaPrezentare.html'
