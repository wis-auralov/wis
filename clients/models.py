from datetime import date
from django.db import models


# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    birth_date = models.DateField()
    image_url = models.URLField()
    score = models.PositiveSmallIntegerField(default=0)

    @property
    def age(self):
        if self.birth_date:
            today = date.today()
            age = today.year - self.birth_date.year - (
            (today.month, today.day) < (self.birth_date.month, self.birth_date.day))
            return age

    def __str__(self):
            return '{} {}'.format(self.first_name, self.last_name)