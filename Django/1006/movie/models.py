from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=80)
    summary = models.TextField()
    running_time = models.DecimalField(max_digits=4, decimal_places=0)
