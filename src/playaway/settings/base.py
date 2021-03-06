"""
Django settings for playaway project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_NAME = 'playaway'


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('PLAYAWAY_DJANGO_SECRET_KEY', 'CHANGE_ME')

# SECURITY WARNING: don't run with debug turned on in production!
debug = os.environ.get('DEBUG', 'false')
DEBUG = debug.lower() == 'true'


ALLOWED_HOSTS = ['localhost',  '127.0.0.1']
allowed_hosts_other = os.environ.get('PLAYAWAY_ALLOWED_HOSTS', '')
if allowed_hosts_other:
    ALLOWED_HOSTS.extend(allowed_hosts_other.split())



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hxutil',
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

ROOT_URLCONF = PROJECT_NAME + '.urls'

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

WSGI_APPLICATION = PROJECT_NAME + '.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('PLAYAWAY_DB_NAME', 'playaway'),
        'USER': os.environ.get('PLAYAWAY_DB_USER', 'playaway'),
        'PASSWORD': os.environ.get('PLAYAWAY_DB_PASSWORD', 'playaway'),
        'HOST': os.environ.get('PLAYAWAY_DB_HOST', 'localhost'),
        'PORT': os.environ.get('PLAYAWAY_DB_PORT', '5432'),
        'ATOMIC_REQUESTS': False,
        'CONN_MAX_AGE': 500,  # permanent connections
    },
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators
'''
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
'''


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.environ.get('PLAYAWAY_STATIC_ROOT', os.path.join(BASE_DIR, 'http_static/'))


# Logging config
_DEFAULT_LOG_LEVEL = os.environ.get('PLAYAWAY_LOG_LEVEL', 'DEBUG')
_LOG_ROOT = os.environ.get('PLAYAWAY_LOG_ROOT', BASE_DIR)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'request_id': {
            '()': 'log_request_id.filters.RequestIDFilter',
        },
    },
    'formatters': {
        'simple': {
            'format': ('%(asctime)s|%(levelname)s [%(filename)s:%(funcName)s]'
                       ' [%(request_id)s] %(message)s')
        },
        'verbose': {
            'format': '%(levelname)s\t%(asctime)s.%(msecs)03dZ\t%(name)s:%(lineno)s\t%(message)s',
            'datefmt': '%Y-%m-%dT%H:%M:%S'
        },
        'syslog': {
            'format': ('%(levelname)s [%(filename)s:%(funcName)s:%(lineno)s]'
                       ' [%(request_id)s] %(message)s')
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'syslog',
            'stream': 'ext://sys.stdout',
            'filters': ['request_id'],
        },
        'errorfile_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'simple',
            'filename': os.path.join(
                _LOG_ROOT,
                'django-errors-{}.log'.format(PROJECT_NAME)),
            'maxBytes': 10485760,  # 10MB
            'backupCount': 7,
            'encoding': 'utf8',
            'filters': ['request_id'],
        },
        'default': {
            'class': 'logging.handlers.WatchedFileHandler',
            'level': _DEFAULT_LOG_LEVEL,
            'formatter': 'verbose',
            'filename': os.path.join(
                _LOG_ROOT,
                'django-{}.log'.format(PROJECT_NAME)),
        },
    },
    'loggers': {
        'playaway': {
            'level': _DEFAULT_LOG_LEVEL,
            'handlers': ['console'],
            'propagate': True
        },
        'root': {
            'level': _DEFAULT_LOG_LEVEL,
            'handlers': ['console'],
        },
    }
}





