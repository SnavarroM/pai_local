"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-mm*r7hm-mce5&sn+-0s&d$8wyr8z=y_ow8l1)r(gi12ng+vop$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True    

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',


    'crispy_forms',
    'extra_views',
    'import_export',


    'insumos',
    'departamentos',
    'user',
    'formularioInsumos',
    'formularioSR',
    'cargos',
    'compras',
    'proveedores',
    'presupuesto',
    'cierreMensual',
    'configuraciones',
    'logs',
    'inventario',
    'notificacionesCorreo',
    'reportes',
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

ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Santiago'

USE_I18N = True

USE_L10N = True

USE_TZ = True

USE_THOUSAND_SEPARATOR = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'pai_staticfiles')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Admin PAI",
    # Welcome text on the login screen
    "welcome_sign": "Bienvenido a PAI",
    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "Admin PAI",
    # Logo to use for your site, must be present in static files, used for brand on top left
    #"site_logo": "books/img/logo.png",
}


#django-import-export
IMPORT_EXPORT_USE_TRANSACTIONS = True

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'


#Formato Fecha
DATE_FORMATO = ['%d-%m-%Y']
DATETIME_FORMATO = ['%d-%m-%Y %H:%i']


#Configuración Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_FILE_PATH = '/tmp/app-messages'
EMAIL_HOST = 'CENADESAIIS.cenabast.cl'
#EMAIL_PORT = '25'
EMAIL_HOST_USER = 'webserver@cenabast.cl'
EMAIL_HOT_PASSWORD = ''
EMAIL_USE_TLS = False


#Configuración Factura Compras
IVA = '19'


TIPO_FORMULARIO = [
    ('', 'Seleccione Tipo Formulario'),
    ('SOLICITUD', 'SOLICITUD'),
    ('RECLAMO', 'RECLAMO'),
]

# Estado Formulario SR (Solicitud-Reclamo)
ESTADO_FORMULARIOSR = [    
    (1, 'INGRESADO'),
    (2, 'DERIVADO'),
    (3, 'RESPONDIDO'),
    (4, 'SOLUCIONADO'),
    (5, 'SIN SOLUCIÓN'),
]


ESTADO_APROBACION_SOLICITUD = [    
    (1, 'EN ESPERA DE V.B JEFE DPTO.'),
    (2, 'EN ESPERA DE V.B JEFE ADMIN. INTER.'),
    (3, 'APROBADO'),
    (4, 'ENTREGADO'),
    (5, 'RECHAZADO'),
]


ETIQUETAS_ESTADOS_FORMULARIOS = [    
    (1, 'badge rounded-pill bg-warning text-dark'),
    (2, 'badge rounded-pill bg-info text-dark'),
    (3, 'badge rounded-pill bg-primary'),
    (4, 'badge rounded-pill bg-success'),
    (5, 'badge rounded-pill bg-danger'),
]


ESTADO = [
    (True, 'Activo'),
    (False, 'Inactivo')
]