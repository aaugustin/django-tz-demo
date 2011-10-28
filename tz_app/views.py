import datetime

from django import http
from django.conf import settings
from django.shortcuts import render
from django.utils import timezone

try:
    import pytz
except ImportError:
    pytz = None

from .models import Name, AutoName

def home(request):
    default_timezone_name = settings.TIME_ZONE
    if pytz:
        timezones = pytz.common_timezones
        alt_timezone = request.session.get('alt_timezone', pytz.utc)
        alt_timezone_name = alt_timezone.zone
    else:
        timezones = []
        alt_timezone = timezone.utc
        alt_timezone_name = 'UTC'

    utc_now = datetime.datetime.utcnow()
    utc_now = utc_now.replace(microsecond=0, tzinfo=timezone.utc)
    local_now = utc_now.astimezone(timezone.get_current_timezone())
    naive_now = utc_now.astimezone(timezone.get_default_timezone())
    if pytz:
        local_now = timezone.get_current_timezone().normalize(local_now)
        naive_now = timezone.get_default_timezone().normalize(naive_now)
    naive_now = naive_now.replace(tzinfo=None)

    names = Name.objects.order_by('-dated')
    auto_names = AutoName.objects.order_by('-created')

    context = {'pytz': pytz}
    context.update(locals())
    return render(request, 'tz_app/home.html', context)

def set_timezone(request, session_key='django_timezone'):
    next = request.REQUEST.get('next', None)
    if not next:
        next = request.META.get('HTTP_REFERER', None)
    if not next:
        next = '/'
    response = http.HttpResponseRedirect(next)
    if pytz and request.method == 'POST':
        timezone = request.POST.get('timezone')
        if timezone:
            request.session[session_key] = pytz.timezone(timezone)
    return response

