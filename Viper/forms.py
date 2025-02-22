from django import forms
from .models import Medicine

class UploadForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = '__all__'
