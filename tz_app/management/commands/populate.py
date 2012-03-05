import datetime
import random

from django.core.management.base import NoArgsCommand
from django.utils import timezone

from ...models import Name

class Command(NoArgsCommand):
    help = 'Creates random Name objects for testing the admin'

    def handle_noargs(self, **options):
        now = timezone.now()
        dates = []
        for days in xrange(-1000, 1000, 20):
            dates.append((now + datetime.timedelta(days=days)).replace(
                    hour=random.randrange(24),
                    minute=random.randrange(60),
                    second=random.randrange(60),
                    microsecond=random.randrange(1000000)))
        for hours in xrange(-200, 200, 4):
            dates.append((now + datetime.timedelta(hours=hours)).replace(
                    minute=random.randrange(60),
                    second=random.randrange(60),
                    microsecond=random.randrange(1000000)))
        for hours in xrange(-40, 40):
            dates.append((now + datetime.timedelta(hours=hours)).replace(
                    minute=random.randrange(60),
                    second=random.randrange(60),
                    microsecond=random.randrange(1000000)))
        Name.objects.bulk_create(Name(name=unicode(i), dated=dated)
                                 for i, dated in enumerate(dates))
        self.stdout.write('Created %d objects\n' % len(dates))