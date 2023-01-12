from django import forms
from .models import Images

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ['file']

