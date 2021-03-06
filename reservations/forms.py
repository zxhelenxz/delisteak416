from django import forms
from .models import Reserve


class ReserveForm(forms.ModelForm):
    class Meta:
        model = Reserve
        fields = ['time', 'date', 'person', 'table']