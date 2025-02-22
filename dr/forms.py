from django import forms

from dr.models import Patient,Drug


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['national_id']

class DrugForm(forms.ModelForm):
    class Meta:
        model = Drug
        fields = ['name','effective_dose','generic_code']
