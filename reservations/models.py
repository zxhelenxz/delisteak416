from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

TABLE_CATEGORY = (
    ('Inside', 'Inside'),
    ('Outside', 'Outside'),
    ('Upstair', 'Upstair'),
    ('Downstair', 'Downstair'),
    ('Window', 'Window'),
)


# Create your models here.
class Reserve(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.TimeField(blank=False)
    date = models.DateField(blank=False)
    person = models.IntegerField(default=1, validators=[MaxValueValidator(50), MinValueValidator(1)])
    table = models.CharField(max_length=30, blank=True, choices=TABLE_CATEGORY)

    def __str__(self):
        return self.id
