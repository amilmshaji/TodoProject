from django.db import models

# Create your models here.
class Task(models.Model):
    name=models.CharField(max_length=250)
    priority=models.IntegerField()
    date=models.DateField()
    def ___str__(self):
        return self.name