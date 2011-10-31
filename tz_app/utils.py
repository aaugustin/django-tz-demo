import datetime

from django.utils import timezone

try:
    import pytz
except ImportError:
    pytz = None

def get_utc_now():
    now = datetime.datetime.utcnow()
    now = now.replace(microsecond=0, tzinfo=timezone.utc)
    return now

def get_default_now():
    return get_now_in(timezone.get_default_timezone())

def get_current_now():
    return get_now_in(timezone.get_current_timezone())

def get_now_in(tz):
    now = get_utc_now().astimezone(tz)
    if pytz:
        now = tz.normalize(now)
    return now
