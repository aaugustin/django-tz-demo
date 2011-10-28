from django.conf import settings
from django.utils import timezone

try:
    import pytz
except ImportError:
    pytz = None

def timezones(request):
    alt_timezone = request.session.get('alt_timezone', pytz.utc)
    return {
        'pytz': pytz,
        'default_timezone_name': settings.TIME_ZONE,
        'timezones': pytz.common_timezones if pytz else [],
        'alt_timezone': alt_timezone if pytz else timezone.utc,
        'alt_timezone_name': alt_timezone.zone if pytz else 'UTC',
    }
