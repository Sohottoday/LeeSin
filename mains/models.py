from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=50)
    scale = models.IntegerField()
    location = models.CharField(max_length=60)
    homepage = models.CharField(max_length=50)

class Recruit(models.Model):
    carear = models.CharField(max_length=50)
    carear_start = models.IntegerField()
    carear_end = models.IntegerField()
    recruit_page = models.CharField(max_length=50)
    uploed = models.TimeField(auto_now=True)
    company = models.ForeignKey(Company,on_delete=models.DO_NOTHING)

class RequireStack(models.Model):
    recruit = models.ForeignKey(Recruit,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

class Stack(models.Model):
    name = models.CharField(max_length=50)
    img = models.CharField(max_length=100)
    detail = models.TextField()
    web_page = models.CharField(max_length=50)