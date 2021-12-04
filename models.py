from django.db import models


# Create your models here.


class Reserve(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    reserve_time = models.TimeField()
    reserve_email = models.EmailField()
    reserve_date = models.DateField()
    reserve_party = models.IntegerField()
