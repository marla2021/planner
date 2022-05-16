"""
Django settings for todolist project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from os import environ
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from dotenv import load_dotenv
from environ import Env

BASE_DIR = Path(__file__).resolve().parent.parent

ALLOWED_HOSTS = ["*"]
env = Env()

env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = env("SECRET_KEY")
DEBUG = env.bool("DEBUG", False)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!


AUTH_USER_MODEL = 'core.User'
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_yasg',
    'django_filters',
    'social_django',
    'todolist',
    'core',
    'goals',
    'bot',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware'
]

ROOT_URLCONF = 'todolist.urls'

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
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect'
            ],
        },
    },
]

WSGI_APPLICATION = 'todolist.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'todolist',
        'USER': 'marla',
        'PASSWORD': os.environ['POSTGRES_PASSWORD'],
        'HOST': os.environ.get('DB_HOST', '127.0.0.1'),
        'PORT': '5432',
    },
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'postgres',
#         'USER': 'postgres',
#         'PASSWORD': 'postgres',
#         'HOST':'localhost',
#         'PORT': '5432',
#     },
# }

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# REST_FRAMEWORK = {
#     # Use Django's standard `django.contrib.auth` permissions,
#     # or allow read-only access for unauthenticated users.
#     'DEFAULT_PAGINATION_CLASS': [
#         'rest_framework.pagination.LimitOffsetPagination',
#     ]
# }


AUTHENTICATION_BACKENDS = (
    "social_core.backends.vk.VKOAuth2",
    "django.contrib.auth.backends.ModelBackend",
)
SOCIAL_AUTH_JSONFIELD_ENABLED = True
SOCIAL_AUTH_URL_NAMESPACE = "social"
SOCIAL_AUTH_VK_OAUTH2_KEY = env("SOCIAL_AUTH_VK_OAUTH2_KEY")
SOCIAL_AUTH_VK_OAUTH2_SECRET = env("SOCIAL_AUTH_VK_OAUTH2_SECRET")
SOCIAL_AUTH_VK_OAUTH2_SCOPE = ["email", "photos", "notify"]
SOCIAL_AUTH_LOGIN_REDIRECT_URL = "/logged-in/"
SOCIAL_AUTH_LOGIN_ERROR_URL = "/login-error/"

BOT_TOKEN = env.str("BOT_TOKEN")

CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOW_CREDENTIALS = True

CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1",
    "http://localhost",
]



















