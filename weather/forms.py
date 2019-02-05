from django.forms import ModelForm
from .models import City


class Cityform(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name']
        
