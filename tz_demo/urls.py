from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'tz_app.views.home', name='home'),
    url(r'^locale/', 'django.views.i18n.set_language', name='set_locale'),
    url(r'^timezone/', 'tz_app.views.set_timezone', name='set_timezone'),
    url(r'^admin/', include(admin.site.urls)),
)
