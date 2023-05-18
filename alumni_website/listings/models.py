""" Creation of models class of the app """
from django.db import models
from django.contrib.auth.models import User


class DiplomaNumber(models.Model):
    """Diploma number data base gestion"""

    diploma_number = models.fields.IntegerField(primary_key=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    year = models.fields.IntegerField()  # Put contraint for being a year
    programe_name = models.fields.CharField(max_length=500)
