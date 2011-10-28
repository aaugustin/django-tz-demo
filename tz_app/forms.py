from django import forms

from .utils import get_utc_now

class WhenForm(forms.Form):
    when = forms.DateTimeField(initial=get_utc_now)
