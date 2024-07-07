from django import forms
from .models import  Routes


class SearchForm(forms.Form):
    source = forms.CharField(label='Source', max_length=100)
    destination = forms.CharField(label='Destination', max_length=100)
class RoutesForm(forms.Form):
    class Meta:
        model=Routes
        fields=['number','Source','Destination','Src','Dest','Stops','departure_time']
