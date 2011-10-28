from django import http
from django.shortcuts import render
from django.utils import timezone

try:
    import pytz
except ImportError:
    pytz = None

from .forms import WhenForm
from .models import Name, AutoName
from .utils import get_utc_now, get_default_now, get_current_now

def home(request):
    utc_now = get_utc_now()
    local_now = get_current_now()
    naive_now = get_default_now().replace(tzinfo=None)

    form = WhenForm(request.GET or None)
    if form.is_valid():
        value = form.cleaned_data['value']
        split_value = form.cleaned_data['split_value']

    names = Name.objects.order_by('-dated')
    auto_names = AutoName.objects.order_by('-created')

    return render(request, 'tz_app/home.html', locals())

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

