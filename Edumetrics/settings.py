

from pathlib import Path
import os
from django.urls import reverse

culipa_headers = {
  'api-key': '9B5930203A974B3B48574E3AFA597BD7DA2E4E0A1C2578B40FA0B1F6526401D2',
  'merchant': 'Edumetrics',
  'Content-Type': 'application/json'
}

my_apps = [
    'Auth',
    'Examinations',
    'Parents',
    'Reports',
    'SchoolAdministrators',
    'Students',
    'Teachers',
    'Edumetrics',
    'Schools',
    'Attendance',
    'Recruitments',
    'Classes',
    'Subjects',
    'Streams',
    'Events',
    'imagekit',
    'Lessons',
    'Grading',
    'Subscriptions',
    'Circulars',
    'Tallies',
    'FeesManagement',
    'Terms',
    'Enrollments',
    'Messages',
]

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_TIMEZONE = 'UTC'
CELERY_BEAT_SCHEDULE = {
    'send-lesson-reminders': {
        'task': 'Auth.tasks.send_lesson_reminders',
        'schedule': 60.0, # Run the task every 1 minute
    },
}



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#4xjdr0@zw4nzy(697deby!li%wop2zkl%vf4hlt$9e$r^*z5('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['192.168.137.1', '127.0.0.1', 'edu-metrics.com', 'mail.edu-metrics.com', 'www.edu-metrics.com']

LOGIN_URL = '/'

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail.edu-metrics.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'info@edu-metrics.com'
EMAIL_HOST_PASSWORD = 'intention12@'
DEFAULT_FROM_EMAIL = 'info@edu-metrics.com'


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Auth',
    'Examinations',
    'Parents',
    'Reports',
    'SchoolAdministrators',
    'Students',
    'Teachers',
    'Edumetrics',
    'Schools',
    'Attendance',
    'Recruitments',
    'Classes',
    'Subjects',
    'Streams',
    'Events',
    'imagekit',
    'Lessons',
    'Grading',
    'Subscriptions',
    'Circulars',
    'Tallies',
    'FeesManagement',
    'Terms',
    'Enrollments',
    'Messages',
    'LibraryManagement',
    'Programmes',
    'SickBay',
    'MarkSheets',
    'Applications',
    'Shop',
    'QuestionBanks',
    'PastPapers',
    'Requirements',
    'Levels',
    'EducationHistory',
    'TeachingHistory',
    'BroadCasts',
    'Payments',
    'channels',
    'Chats',
]

ASGI_APPLICATION = "Edumetrics.asgi.application"

CRISPY_TEMPLATE_PACK = 'bootstrap4'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
     'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'Edumetrics.session_middleware.SessionMiddleware',
    'Edumetrics.nocache_middleware.NoCacheMiddleware' 
]

CORS_ORIGIN_ALLOW_ALL = True


ROOT_URLCONF = 'Edumetrics.urls'

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
                'Edumetrics.context_processors.renders_processor'
            ],
        },
    },
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

WSGI_APPLICATION = 'Edumetrics.wsgi.application'



# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'edumetrics_database',
        'USER': 'edumetrics_user',
        'PASSWORD': 'intention12@',
        'HOST': 'edu-metrics.com',
        'PORT': '3306',
        'OPTIONS': {
            'sql_mode': 'STRICT_TRANS_TABLES',
        },
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Kampala'
    

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

MEDIA_URL = ''
MEDIA_ROOT = os.path.join(BASE_DIR, '')

STATIC_URL = '/static/'

if not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'Edumetrics/static'),
]


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
