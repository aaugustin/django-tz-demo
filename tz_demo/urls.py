from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('tz_app.views',
    url(r'^$', 'home', name='home'),
    url(r'^timezone/', 'set_timezone', name='set_timezone'),
    url(r'^alt_timezone/', 'set_timezone', name='set_alt_timezone',
                kwargs={'key': 'alt_timezone', 'name': 'alternative'}),
    url(r'^locale/', 'set_locale', name='set_locale'),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
