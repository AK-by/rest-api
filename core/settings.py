import os
from os.path import join, dirname
from pathlib import Path
from dotenv import load_dotenv

# Отображать ошибки на сайте (только для разработки)
DEBUG = False

# Переменные в окружении
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Полный путь к проекту: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
REPOSITORY_ROOT = os.path.dirname(BASE_DIR)

# Ключ доступа к проекту, поменять перед установкой на сервер
SECRET_KEY = os.getenv("SECRET_KEY")

# Разрешенные доменные имена (хосты)
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS").split()

# Наше серверное приложение маршрутизации
WSGI_APPLICATION = 'core.wsgi.application'

# Основной файл Urls
ROOT_URLCONF = 'core.urls'

# Auth
LOGIN_URL = '/sign-in/'
LOGIN_REDIRECT_URL = '/'

# Rest
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_FILTER_BACKEND': (
        'django_filters.rest_framework.DjangoFilterBackend'
    ),
    'DEFAULT_PAGINATION_CLASS': (
        'rest_framework.pagination.LimitOffsetPagination'
    ),
    'PAGE_SIZE': 2,
}

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("DATABASE_NAME"),
        'USER': os.getenv("DATABASE_USER"),
        'PASSWORD': os.getenv("DATABASE_PASSWORD"),
        'PORT': os.getenv("DATABASE_PORT"),
    }
}

# Установленные приложения
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_filters',
    'core',
    'restapi',
]

# Установленные плагины и библиотеки
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Шаблоны
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/4.2/topics/i18n/
DEFAULT_AUTO_FIELD = os.getenv("DEFAULT_AUTO_FIELD")
DATE_INPUT_FORMATS = os.getenv("DATE_INPUT_FORMATS").split()
USE_L10N = bool(os.getenv("USE_L10N"))
LANGUAGE_CODE = os.getenv("LANGUAGE_CODE")
TIME_ZONE = os.getenv("TIME_ZONE")
USE_I18N = bool(os.getenv("USE_I18N"))
USE_TZ = bool(os.getenv("USE_TZ"))

# Static files (CSS, JavaScript, Images)
STATIC_URL = os.getenv("STATIC_URL")
MEDIA_URL = os.getenv("MEDIA_URL")

if DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
else:
    STATIC_ROOT = '/var/www/rest-api/static/'
    MEDIA_ROOT = '/var/www/rest-api/media/'
