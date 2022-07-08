from django.contrib import admin
from django.urls import path, include
from SistemdeConectare import views
from django.contrib.auth import views as autentificare_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Despre/', views.Despre, name="SistemdeConectare-Despre"),
    path('Inregistrare/', views.Inregistrare, name='Inregistrare'),
    path('login/', autentificare_views.LoginView.as_view(template_name = 'SistemdeConectare/Conectare.html'), name="Conectare"),
    path('logout/', autentificare_views.LogoutView.as_view(template_name = 'SistemdeConectare/Deconectare.html'), name="Deconectare"),
    path('password-reset/', autentificare_views.PasswordResetView.as_view(template_name = 'SistemdeConectare/password_reset.html'), name="password_reset"),
    path('password-reset/done/', autentificare_views.PasswordResetDoneView.as_view(template_name = 'SistemdeConectare/password_reset_done.html'), name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>', autentificare_views.PasswordResetConfirmView.as_view(template_name = 'SistemdeConectare/password_reset_confirm.html'), name="password_reset_confirm"),
    path('password-reset-complete/', autentificare_views.PasswordResetCompleteView.as_view(template_name = 'SistemdeConectare/password_reset_complete.html'), name="password_reset_complete"),
    path('', include('Gestiune.urls')),
    path('', include('Facturare.urls')),
]
