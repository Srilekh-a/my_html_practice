from django import forms
from .models import student1

class std_form(forms.ModelForm):
    class Meta:
        model=student1
        fields=["std_name","std_lastname","std_address"]
