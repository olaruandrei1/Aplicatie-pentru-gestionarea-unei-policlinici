from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-e74_=x0gz&ca4$#n6r_dab@k7+mtulp)ijmdn!51r%_47mdnny'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'jazzmin',
    'Gestiune.apps.GestiuneConfig',
    'SistemdeConectare.apps.SistemdeconectareConfig',
    'Facturare.apps.FacturareConfig',
    'bulma',
    'crispy_forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'HOS.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'HOS.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'HOS',
        'USER': 'postgres',
        'PASSWORD': 'leucoplast',
        'HOST': 'localhost',
        'POST': '5432',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'


TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = 'Gestiune-PaginaPrincipala'
LOGIN_URL = 'Conectare'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'holaruservices@gmail.com'
EMAIL_HOST_PASSWORD = 'jknahaovaexqdblf'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'default from email'


JAZZMIN_SETTINGS = {
"site_title": "HOS",
"site_header": "HOS",
"login_logo": "{% static 'Gestiune/Imagini/logo.ico' %}",
"site_icon": "{% static 'Gestiune/Imagini/logo.ico' %}",
"related_modal_active": True,

}
JAZZMIN_UI_TWEAKS = {

    "theme": "cyborg",
}
