"""
Generated by 'django-admin startproject' using Django 3.2.9.

"""
import pathlib
from pathlib import Path
import os
import json
from django.contrib.messages import constants as messages

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-cb8gf3co*s@b^ql80r@=vz8zlrn2pe5-33d7_(x*h8_qt3@l(t'

# for testing local_config
with open(BASE_DIR / 'nest' / 'config.json') as fh:
    local_config = json.load(fh)

DEBUG = True

ALLOWED_HOSTS = []

AUTH_USER_MODEL = "fam.User"

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # third parties
    'debug_toolbar',
    'bootstrap4',
    # custom
    'fam.apps.FamConfig',
    'commons.apps.CommonsConfig',
    'books.apps.BooksConfig',
    'purchases.apps.PurchasesConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'nest.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'nest.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# # send grid
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = config.get('MY_EMAIL')
EMAIL_HOST_PASSWORD = config.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
ACCOUNT_EMAIL_SUBJECT_PREFIX = "Greetings from training site  "
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
INTERNAL_IPS = ['127.0.0.1']

STATIC_URL = '/static/'
STATICFILES_DIRS = (BASE_DIR.joinpath('static'),)
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# if 'test' in sys.argv:
#     print('line 122')
#     DATABASES['default'] = {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': local_config.get('NAME'),
#         'USER': local_config.get('USER'),
#         'PASSWORD': local_config.get('PASSWORD'),
#         'HOST': '127.0.0.1',
#         'PORT': '5432'
#     }