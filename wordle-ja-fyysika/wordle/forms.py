from django import forms
from django.core.exceptions import ValidationError
from views2 import validate_letter


class LetterForm(forms.Form):
    input = forms.CharField(validators=[validate_letter])