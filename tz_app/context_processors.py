from django.conf import settings
from django.utils import timezone
from django.utils import six

try:
    import pytz
except ImportError:
    pytz = None

def timezones(request):
    other_timezone = request.session.get('other_timezone', (pytz or timezone).utc)
    if pytz is not None and isinstance(other_timezone, six.text_type):
        other_timezone = pytz.timezone(other_timezone)
    return {
        'pytz': pytz,
        'default_timezone_name': settings.TIME_ZONE,
        'timezones': pytz.common_timezones if pytz else [],
        'other_timezone': other_timezone if pytz else timezone.utc,
        'other_timezone_name': other_timezone.zone if pytz else 'UTC',
    }
