from django.db import models

# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=50)
    scale = models.IntegerField()
    location = models.CharField(max_length=60)
    homepage = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Recruit(models.Model):
    carear = models.CharField(max_length=50)
    carear_start = models.IntegerField()
    carear_end = models.IntegerField()
    recruit_page = models.CharField(max_length=50)
    uploed = models.TimeField(auto_now=True)
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)


class RequireStack(models.Model):
    recruit = models.ForeignKey(Recruit, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    is_now = models.BooleanField(default=True)


class Stack(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    img = models.CharField(max_length=100, null = True)
    detail = models.TextField(null = True)
    web_page = models.CharField(max_length=50, null = True)
    created_at = models.DateTimeField(auto_now_add=True, null = True)
    updated_at = models.DateTimeField(auto_now=True, null = True)