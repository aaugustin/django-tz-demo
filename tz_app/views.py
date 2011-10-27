from django.shortcuts import render
from django import http

try:
    import pytz
except ImportError:
    pytz = None

from .models import Name, AutoName

def home(request):
    if pytz:
        timezones = pytz.common_timezones
    names = Name.objects.order_by('-dated')
    auto_names = AutoName.objects.order_by('-created')
    context = {}
    context.update(globals())
    context.update(locals())
    return render(request, 'tz_app/home.html', context)

def set_timezone(request):
    next = request.REQUEST.get('next', None)
    if not next:
        next = request.META.get('HTTP_REFERER', None)
    if not next:
        next = '/'
    response = http.HttpResponseRedirect(next)
    if pytz and request.method == 'POST':
        timezone = request.POST.get('timezone')
        if timezone:
            request.session['django_time_zone'] = pytz.timezone(timezone)
    return response

