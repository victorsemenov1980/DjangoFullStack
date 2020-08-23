from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Main(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    Name=models.CharField(max_length=255, blank=False)
    Email=models.CharField(max_length=255,blank=False)
    Phone=models.CharField(max_length=255,blank=False)
    Instrument=models.CharField(max_length=255,blank=False)
    Organization=models.CharField(max_length=255,blank=False)
    CoverLetter=models.TextField(blank=False)
    Bio=models.TextField(blank=False)
    Photo=models.ImageField(upload_to='images/',blank=False)
    IsValid=models.BooleanField(default=False)
    
    def summary(self):
        return self.CoverLetter[:100]
    
    def __str__(self):
        return self.Name
    
class Services(models.Model):
    Category=models.CharField(max_length=255,blank=False)
    Sub_Category=models.CharField(max_length=255,blank=True)

class Service(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    Category=models.CharField(max_length=255,blank=True)
    Sub_Category=models.CharField(max_length=255,blank=True)
    Description=models.CharField(max_length=255,blank=True)
    


class FAQ(models.Model):
    Questions=models.TextField(blank=False)
    Answers=models.TextField(blank=False)

class Info(models.Model):
    Message=models.TextField(blank=False)
    
    
    
    
    
    