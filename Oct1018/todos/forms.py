from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    due_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Todo
        fields = ('content', 'due_date',)