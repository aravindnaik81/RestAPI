from django.db import models

# Create your models here.

class ContactBook(models.Model):
    Name = models.CharField(max_length=50)
    Phone_Number = models.CharField(max_length=10,primary_key=True)
    Address = models.CharField(max_length=50)
    SIM = models.CharField(max_length=20)