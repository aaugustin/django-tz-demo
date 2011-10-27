from django.shortcuts import render

try:
    import pytz
except ImportError:
    pytz = None

from .models import Name, AutoName

def home(request):
    names = Name.objects.order_by('-dated')
    auto_names = AutoName.objects.order_by('-created')
    context = {}
    context.update(globals())
    context.update(locals())
    return render(request, 'tz_app/home.html', context)
