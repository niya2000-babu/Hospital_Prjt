from django.db import models


# Create your models here.
class adddepartments(models.Model):
    Department = models.CharField(max_length=50)


class assigndoctor(models.Model):
    Name = models.CharField(max_length=25)
    Contact=models.BigIntegerField()
    Email=models.CharField(max_length=25)
    Symptoms = models.CharField(max_length=50)
    Department = models.CharField(max_length=100)
    Doctor = models.CharField(max_length=100)





