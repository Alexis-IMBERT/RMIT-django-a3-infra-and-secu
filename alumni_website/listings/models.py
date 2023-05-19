""" Creation of models class of the app """
from django.db import models
from django.contrib.auth.models import User



# class DiplomaNumberManager(models.Manager):
#     """ Diploma Manager """
#     def create_diploma(self, diploma_number, username, year, programe_name):
#         """ create a new diploma """
#         diploma = self.create(diploma_number=diploma_number, username=username, year=year, programe_name=programe_name)
#         # do something with the diploma 
#         return diploma


class DiplomaNumber(models.Model):
    """Diploma number data base gestion"""

    diploma_number = models.fields.CharField(primary_key=True, max_length=7)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    year = models.fields.IntegerField()  # Put contraint for being a year
    programe_name = models.fields.CharField(max_length=500)

    # objects = Dhttps://calendar.google.com/calendar/ical/alexis.imbert75%40gmail.com/private-de8b575eeb0f3b7b36dd55d85689e2cd/basic.icsiplomaNumberManager()
