from django.db import models

# Create your models here.
class Register(models.Model):
    Name=models.CharField(max_length=25)
    Age=models.DateField()
    Phone = models.BigIntegerField()
    Gender=models.CharField(max_length=10)
    Address=models.CharField(max_length=50)
    Username = models.CharField(max_length=25)
    Password = models.CharField(max_length=15)
    Status = models.CharField(max_length=20, default='')


class Login(models.Model):
    Username = models.CharField(max_length=25)
    Password = models.CharField(max_length=15)

    Usertype = models.CharField(max_length=20)

class appointment(models.Model):
    Name=models.CharField(max_length=20)
    Contact=models.CharField(max_length=20)
    Date=models.DateField(null=True, blank=True)
    Email = models.CharField(max_length=30)
    Symptoms=models.CharField(max_length=250, null=True, blank=True)
    status=models.CharField(max_length=20, default='')


class pay(models.Model):
    BankName=models.CharField(max_length=25)
    Branch=models.CharField(max_length=25)
    IFSC=models.CharField(max_length=25)
    cardholder = models.CharField(max_length=200)
    amount = models.IntegerField()