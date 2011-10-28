from django import forms

from .utils import get_utc_now

class WhenForm(forms.Form):
    value = forms.DateTimeField(initial=get_utc_now, required=False)
    split_value = forms.SplitDateTimeField(initial=get_utc_now, required=False)
