from django.db import models


# Create your models here.

class Student(models.Model):
    id = models.CharField(primary_key=True, max_length=9)
