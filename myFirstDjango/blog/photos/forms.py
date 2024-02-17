from django import forms
from django.forms import widgets


class PhotoUploadForm(forms.Form):
    image = forms.ImageField(
        # widget=widgets.FileInput(attrs={"multiple": "multiple"})
    )
