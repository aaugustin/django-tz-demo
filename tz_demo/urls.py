from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('tz_app.views',
    url(r'^$', 'home', name='home'),
    url(r'^timezone/', 'set_timezone', name='set_timezone'),
    url(r'^other_timezone/', 'set_timezone', name='set_other_timezone',
                kwargs={'key': 'other_timezone', 'name': 'alternative'}),
    url(r'^locale/', 'set_locale', name='set_locale'),
)

urlpatterns += patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
