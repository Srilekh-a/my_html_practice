from django import forms
from .models import list

class TaskForm(forms.ModelForm):
    class meta:
        model='list'
        fields=['title']
        
