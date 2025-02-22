from django.contrib.auth.models import AbstractUser
from django.db import models
from dr.models import Patient

# Create your models here.

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    effective_dose = models.IntegerField()
    generic_name = models.CharField(max_length=100)
    generic_code = models.CharField(max_length=10, verbose_name="Generic Code",null=True,blank=True)
    pharmaceutical_form = models.CharField(max_length=100)
    description = models.TextField()
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='medicines/')

    def get_url(self):
        return str(self.image.url)

    def __str__(self):
        return f'{self.name}, {self.effective_dose}'

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    def __str__(self):
        return f'{self.name}, {self.email}'

#

class PatientMedicine(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.patient.national_id}, {self.medicine}'





