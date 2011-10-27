This is a sample Django project to demonstrate timezone support. To run it:

$ hg clone https://bitbucket.org/aaugustin/django
$ hg clone https://bitbucket.org/aaugustin/django-tz-demo
$ cd django-tz-demo
$ PYTHONPATH=../django python manage.py syncdb --noinput
$ PYTHONPATH=../django python manage.py runserver

You will get more interesting results if you install pytz.
