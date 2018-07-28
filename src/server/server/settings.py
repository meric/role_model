"""
Django settings for server project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import sys

from sqlalchemy.dialects.postgresql import UUID


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ik!xl@%o7b()9vv5b_xb%uxjlg-t58x0t2^b75^9h_9bz@nhs5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# https://stackoverflow.com/questions/6957016/detect-django-testing-mode
TEST = sys.argv[1:2] == ['test']

ALLOWED_HOSTS = []

AUTH_USER_MODEL = 'crm.User'
ROLE_MODEL_ORGANIZATION_MODEL = 'crm.Organization'

# ALDJEMY
ALDJEMY_DATA_TYPES = {
    'UUIDField': lambda field: UUID()
}

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'common',
    'crm',
    'role_model',
    'django_extensions',
    'graphene_django',
    'django.contrib.sites',
    'server',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'aldjemy',
    'history',
    'network_graph',
    'debug_toolbar',
]

SITE_ID = 1
SITE_DOMAIN = 'localhost:8000'
SITE_NAME = 'role model'

ALLAUTH_GOOGLE_SOCIALAPP_ID = 1
ALLAUTH_GOOGLE_SOCIALAPP_NAME = "Google"
ALLAUTH_GOOGLE_SOCIALAPP_CLIENT_ID = 1
ALLAUTH_GOOGLE_SOCIALAPP_SECRET_KEY = 1

HISTORY_MODELS = [
    'role_model.Assignment',
    'role_model.ContentType',
    'role_model.Deliverable',
    'role_model.Facet',
    'role_model.Format',
    'role_model.Group',
    'role_model.Responsibility',
    'role_model.Role',
    'crm.Organization',
    'crm.User'
]

# SocialApp

GRAPHENE = {
    'SCHEMA': 'role_model.schema.schema'
}

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

INTERNAL_IPS = ['127.0.0.1']

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

ROOT_URLCONF = 'server.urls'

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

WSGI_APPLICATION = 'server.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'role_model',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Australia/Sydney'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static'
