from django import forms
from .models import Coffee, Flavor

class CoffeeForm(forms.ModelForm):
    class Meta:
        model = Coffee
        fields = '__all__'

class FlavorForm(forms.ModelForm):
    class Meta:
        model = Flavor
        fields = ('star', 'memo',)