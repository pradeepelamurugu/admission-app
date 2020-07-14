from django.db import models

# Create your models here.
class Staff(models.Model):
    approved = models.BooleanField()
    rejected = models.BooleanField()

