from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    national_code = models.CharField(max_length=10, unique=True, verbose_name="National_Code")
    def __str__(self):
        return self.username
