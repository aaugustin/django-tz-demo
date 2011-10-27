from django.shortcuts import render

try:
    import pytz
except ImportError:
    pytz = None

def home(request):
    context = {}
    context.update(globals())
    context.update(locals())
    return render(request, 'tz_app/home.html', context)
