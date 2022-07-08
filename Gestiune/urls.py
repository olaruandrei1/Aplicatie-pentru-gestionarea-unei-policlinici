from django.urls import path, include
from Gestiune import views
from .views import *

urlpatterns = [
	path('', views.PaginadeStart, name='Gestiune-PaginadeStart'),
	path('PaginaPrincipala/', PacientiListView.as_view(), name='Gestiune-PaginaPrincipala'),
	path('PaginaAdaugarePacient/new/', PacientiCreateView.as_view(), name='Gestiune-PaginaAdaugarePacient'),
	path('PaginaVizualizarePacient/<int:pk>/', PacientiDetailView.as_view(), name='Gestiune-PaginaVizualizarePacient'),
	path('PaginaVizualizarePacient/<int:pk>/update/', PacientiUpdateView.as_view(), name='Gestiune-PaginaEditarePacient'),
	path('PaginaStergerePacient/<int:pk>/delete/', PacientiDeleteView.as_view(), name='Gestiune-PaginaStergerePacient'),

	path('PaginaAdaugareInternare/new/', InternareCreateView.as_view(), name='Gestiune-PaginaAdaugareInternare'),
	path('PaginaVizualizareFisaInternare/<int:pk>/', InternareDetailView.as_view(), name='Gestiune-PaginaVizualizareFisaInternare'),
	path('PaginaVizualizareFisaInternare/<int:pk>/update/', InternareUpdateView.as_view(), name='Gestiune-PaginaEditareFisaInternare'),
	path('PaginaStergereFisaInternare/<int:pk>/delete/', InternareDeleteView.as_view(), name='Gestiune-PaginaStergereFisaInternare'),

	path('PaginaAdaugaFisaPrezentare/new/', PrezentareCreateView.as_view(), name='Gestiune-PaginaAdaugaFisaPrezentare'),
	path('PaginaVizualizareFisaPrezentare/<int:pk>/', PrezentareDetailView.as_view(), name='Gestiune-PaginaVizualizareFisaPrezentare'),
	path('PaginaVizualizareFisaPrezentare/<int:pk>/update/', PrezentareUpdateView.as_view(), name='Gestiune-PaginaEditareFisaPrezentare'),
	path('PaginaStergereFisaPrezentare/<int:pk>/delete/', PrezentareDeleteView.as_view(), name='Gestiune-PaginaStergereFisaPrezentare'),

	path('PaginaOpis/', PrezentariListView.as_view(), name='Gestiune-PaginaOpis'),
	path('PaginaOpisInternari/', InternareListView.as_view(), name='Gestiune-PaginaOpisInternari'),

	path('Contact/', views.Contact, name='Gestiune-Contact'),
	path('', include('Facturare.urls')),

]
