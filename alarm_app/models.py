from django.db import models

# Create your models here.
class Alarm(models.Model):
    date_time=models.DateTimeField(null=True)
    days=models.CharField(max_length=50)
