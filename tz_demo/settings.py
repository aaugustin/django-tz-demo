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
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
)

LANGUAGE_CODE = 'en'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'tz_app.middleware.TimezoneMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'tz_app.middleware.AutoLoginMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'tz_demo.urls'

SECRET_KEY = '%u*u4d7%9nk9y1j18%pid_pvm=)zwx#g-n-ov)h(3e975wu#r0'

TEMPLATE_CONTEXT_PROCESSORS = (
   'django.contrib.auth.context_processors.auth',
   'django.core.context_processors.debug',
   'django.core.context_processors.i18n',
   'django.core.context_processors.media',
   'django.core.context_processors.static',
   'django.core.context_processors.tz',
   'tz_app.context_processors.timezones',
)

SITE_ID = 1

STATIC_URL = '/static/'

USE_I18N = True

USE_L10N = True

USE_TZ = True

WSGI_APPLICATION = 'tz_demo.wsgi.application'
