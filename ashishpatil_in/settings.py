"""
Django settings for ashishpatil_in project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from os.path import join as pjoin

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p4t(+by4n-^vhe+5@9lg784xsivib&f&%-s7p2bn(axn7j&u@$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap3',
    #'django.contrib.sites',
    #'allauth',
    #'allauth.account',
    #'allauth.socialaccount',
    #'allauth.socialaccount.providers.facebook',
    #'allauth.socialaccount.providers.twitter',
    #'allauth.socialaccount.providers.google',
    'blog',
    'resume',
    #'storages',
)

#SITE_ID = 1

#ACCOUNT_AUTHENTICATION_METHOD = "username_email"
#ACCOUNT_EMAIL_REQUIRED = True


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

#TEMPLATE_CONTEXT_PROCESSORS = (

    # Required by `allauth` template tags
#    "django.core.context_processors.request",
#    "django.contrib.auth.context_processors.auth",

    # `allauth` specific context processors
#    "allauth.account.context_processors.account",
#    "allauth.socialaccount.context_processors.socialaccount",

#)

#AUTHENTICATION_BACKENDS = (

    # Needed to login by username in Django admin, regardless of `allauth`
#    "django.contrib.auth.backends.ModelBackend",

    # `allauth` specific authentication methods, such as login by e-mail
#    "allauth.account.auth_backends.AuthenticationBackend",

#)

MEDIA_URL = '/media/'
MEDIA_ROOT = pjoin(BASE_DIR, "media")


ROOT_URLCONF = 'ashishpatil_in.urls'

WSGI_APPLICATION = 'ashishpatil_in.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    #'/var/www/static/',
]

#STATIC_ROOT = os.path.join(
#                  os.path.dirname(
#                      os.path.dirname(
#                          os.path.abspath(__file__)
#                      )
#                  ),
#STATIC_ROOT =                  'static'
             # )

STATIC_ROOT = os.path.join(BASE_DIR, '..','static')

if not DEBUG:
    AWS_STORAGE_BUCKET_NAME = 'elasticbeanstalk-us-west-2-917875441687'
    AWS_ACCESS_KEY_ID = 'AKIAIIWYKVNPWLIHTYGQ'
    AWS_SECRET_ACCESS_KEY = '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'
    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
    STATIC_URL = S3_URL
