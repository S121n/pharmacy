from django.db import models

class Patient(models.Model):
    national_id = models.CharField(max_length=50, unique=True, verbose_name="National ID")

    def __str__(self):
        return self.national_id

class Drug(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="drugs")
    name = models.CharField(max_length=100, verbose_name="Drug Name")
    effective_dose = models.CharField(max_length=50, verbose_name="Effective Dose", null=True, blank=True)
    generic_code = models.CharField(max_length=10, verbose_name="Generic Code", null=True, blank=True)

    def __str__(self):
        return f"{self.name} , {self.effective_dose} , ({self.generic_code})"
