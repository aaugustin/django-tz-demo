from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('tz_app.views',
    url(r'^$', 'home', name='home'),
    url(r'^timezone/', 'set_timezone', name='set_timezone'),
    url(r'^alt_timezone/', 'set_timezone', {'session_key': 'alt_timezone'},
            name='set_alt_timezone'),
)

urlpatterns += patterns('',
    url(r'^locale/', 'django.views.i18n.set_language', name='set_locale'),
    url(r'^admin/', include(admin.site.urls)),
)
