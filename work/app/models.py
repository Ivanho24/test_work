from django.db import models
from django.utils import timezone

class JSONData(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField(default=timezone.now)


class Meta:
    ordering = ('-publish',)

def __str__(self):
    return self.title