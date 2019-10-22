from django import forms
from .models import Big, Small, Hashtag

class BigForm(forms.ModelForm):
    class Meta:
        model = Big
        fields = '__all__'

class SmallForm(forms.ModelForm):
    class Meta:
        model = Small
        fields = '__all__'

class HashtagForm(forms.ModelForm):
    class Meta:
        model = Hashtag
        fields = ('content',)