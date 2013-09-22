from django.contrib import messages
from django.shortcuts import redirect, render
from django.utils import timezone
from django.utils import translation
from django.views.decorators.http import require_POST, require_safe

try:
    import pytz
except ImportError:
    pytz = None

from .forms import WhenForm
from .models import Name, AutoName
from .utils import get_utc_now, get_default_now, get_current_now

@require_safe
def home(request):
    utc_now = get_utc_now()
    local_now = get_current_now()
    naive_now = get_default_now().replace(tzinfo=None)

    form = WhenForm(request.GET or None)
    if form.is_valid():
        value = form.cleaned_data['value']
        split_value = form.cleaned_data['split_value']

    names = Name.objects.order_by('dated')
    auto_names = AutoName.objects.order_by('created', 'updated')

    return render(request, 'tz_app/home.html', locals())

@require_POST
def set_timezone(request, key='django_timezone', name='current'):
    timezone = request.POST.get(key)
    if pytz and timezone:
        try:
            pytz.timezone(timezone)
        except pytz.UnknownTimeZoneError:
            messages.error(request, "Time zone '%s' isn't available." % timezone)
        else:
            messages.info(request, "The %s time zone was set to '%s'."
                                   % (name, timezone))
            request.session[key] = timezone
    return redirect(request.META.get('HTTP_REFERER') or home)

@require_POST
def set_locale(request):
    lang_code = request.POST.get('language')
    if lang_code:
        if translation.check_for_language(lang_code):
            request.session['django_language'] = lang_code
            messages.info(request, "The locale was set to '%s'." % lang_code)
        else:
            messages.error(request, "Locale '%s' isn't available." % lang_code)
    return redirect(request.META.get('HTTP_REFERER') or home)
