from django import forms
from .models import Part


class PartForm(forms.ModelForm):
    class Meta:
        model = Part
        fields = ["name", "category", "brand", "price", "build", "notes"]
        
        