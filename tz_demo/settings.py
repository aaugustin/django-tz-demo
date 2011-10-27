# Django settings for tz_demo project.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

DATETIME_FORMAT = 'c'

DEBUG = True

INSTALLED_APPS = (
    'tz_app',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
)

ROOT_URLCONF = 'tz_demo.urls'

SECRET_KEY = '%u*u4d7%9nk9y1j18%pid_pvm=)zwx#g-n-ov)h(3e975wu#r0'

SITE_ID = 1

STATIC_URL = '/static/'

USE_I18N = False

USE_L10N = False

USE_TZ = True

WSGI_APPLICATION = 'tz_demo.wsgi.application'
