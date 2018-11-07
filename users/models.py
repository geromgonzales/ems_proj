from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class Participant(AbstractUser):
    contact_number = models.CharField("contact Number", max_length = 20)

    def __str__(self):
        return self.username
