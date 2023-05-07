from django.db import models


class Alumni(models.Model):
    """ Alumni's class definition """
    username = models.fields.CharField(max_length=100)  # Username of the alumni
    diploma_number = models.fields.BigIntegerField()  # Number of the diploma 
                                                    # password will be hash in the future
    password = models.fields.CharField(max_length=100)

    def __str__(self):
        return f'{self.username}'
