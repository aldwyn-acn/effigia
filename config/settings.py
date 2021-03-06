"""
Django settings for effigia project.

Generated by 'django-admin startproject' using Django 1.11.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from django.core.exceptions import ImproperlyConfigured
from django.urls import reverse_lazy


def get_env_variable(var_name):
    """ Get the environment variable or return exception """
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wdmfxchl(qb-uf-q3g#zbo3*ordjlls1(+6*$rbik(2%((y36#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# ALLOWED_HOSTS = ['ubuntubitch', 'localhost', '127.0.0.1']
ALLOWED_HOSTS = ['*']

INTERNAL_IPS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    # 'wpadmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.twitter',
    'avatar',
    'debug_toolbar',
    'django_countries',
    'django_nose',
    # 'easy_timezones',
    'imagekit',
    'ordered_model',
    'storages',
    'core',
    'apps.accounts',
    'apps.chats',
    'apps.dashboard',
    'apps.galleries',
    'apps.groups',
    'apps.interactions',
    'apps.portfolios',
    'apps.posts',
    'actstream',
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
    # 'easy_timezones.middleware.EasyTimezoneMiddleware',
    'core.middlewares.common.EffigiaVisitMiddleware',
]

SITE_ID = 1

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_env_variable('DJANGO_DB_NAME'),
        'USER': get_env_variable('DJANGO_DB_USER'),
        'PASSWORD': get_env_variable('DJANGO_DB_PASS'),
        'HOST': get_env_variable('DJANGO_DB_HOST'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


AUTH_USER_MODEL = 'accounts.User'

# GEOIP_DATABASE = os.path.join(BASE_DIR, 'core/resources/GeoLiteCity.dat')
# GEOIPV6_DATABASE = os.path.join(BASE_DIR, 'core/resources/GeoLiteCity.dat')

LOGIN_URL = reverse_lazy('account_login')
LOGOUT_URL = reverse_lazy('account_logout')
LOGIN_REDIRECT_URL = reverse_lazy('dashboard:home')
LOGOUT_REDIRECT_URL = reverse_lazy('core:index')

STATIC_URL = get_env_variable('DJANGO_STATIC_URL')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

MEDIA_URL = get_env_variable('DJANGO_MEDIA_URL')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_FILE_STORAGE = get_env_variable('DJANGO_FILE_STORAGE_BACKEND')

GS_BUCKET_NAME = get_env_variable('GS_BUCKET_NAME')
GS_FILE_OVERWRITE = False

DJANGO_ADMIN_PASS = get_env_variable('DJANGO_ADMIN_PASS')

# ACTSTREAM_SETTINGS = {
#     'MANAGER': 'core.managers.EffigiaActionManager'
# }

# django-allauth
ACCOUNT_SESSION_REMEMBER = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_SUBJECT_PREFIX = '[effigia.com] '
ACCOUNT_USERNAME_MIN_LENGTH = 4
ACCOUNT_USERNAME_BLACKLIST = ['admin']
ACCOUNT_LOGOUT_ON_GET = True

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': ['profile', 'email', ],
        'AUTH_PARAMS': {'access_type': 'online'}
    },
    'facebook': {
        'SCOPE': ['email', 'public_profile', 'user_friends'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
    },
    'twitter': {
        'SCOPE': ['profile', 'email'],
    }
}

GOOGLE_OAUTH2_CLIENT_ID = get_env_variable('GOOGLE_OAUTH2_CLIENT_ID')
GOOGLE_OAUTH2_CLIENT_SECRET = get_env_variable('GOOGLE_OAUTH2_CLIENT_SECRET')

FACEBOOK_OAUTH2_CLIENT_ID = get_env_variable('FACEBOOK_OAUTH2_CLIENT_ID')
FACEBOOK_OAUTH2_CLIENT_SECRET = get_env_variable('FACEBOOK_OAUTH2_CLIENT_SECRET')

TWITTER_OAUTH2_CLIENT_ID = get_env_variable('TWITTER_OAUTH2_CLIENT_ID')
TWITTER_OAUTH2_CLIENT_SECRET = get_env_variable('TWITTER_OAUTH2_CLIENT_SECRET')

EMAIL_HOST = 'smtp.mailgun.org'
EMAIL_PORT = 587
EMAIL_HOST_USER = get_env_variable('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = get_env_variable('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True

DEBUG = True
if not os.getenv('GAE_INSTANCE'):
    EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
