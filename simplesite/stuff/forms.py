from django import forms
from stuff.models import Thing

class StuffForm(forms.ModelForm):

    class Meta:
        model = Thing
        # uncomment the below line to include only specific fields.
        # fields = ('title', 'description')
