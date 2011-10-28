from django.contrib.auth import authenticate, login
from django.utils import timezone

class TimezoneMiddleware(object):

    def process_request(self, request):
        tz = request.session.get('django_timezone')
        if tz is not None:
            timezone.activate(tz)

    def process_response(self, request, response):
        timezone.deactivate()
        return response


class AutoLoginMiddleware(object):

    def process_request(self, request):
        if not request.user.is_authenticated():
            user = authenticate(username='admin', password='password')
            if user is not None:
                login(request, user)
