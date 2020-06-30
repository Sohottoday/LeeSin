from django.db import models

# Create your models here.
class CountIssue(models.Model):
    javascript = models.CharField(max_length=20)
    java = models.CharField(max_length=20)
    python = models.CharField(max_length=20)
    c = models.CharField(max_length=20)
    csharp = models.CharField(max_length=20)
    cplus = models.CharField(max_length=20)
    go = models.CharField(max_length=20)
    ruby = models.CharField(max_length=20)
    typescript = models.CharField(max_length=20)
    php = models.CharField(max_length=20)
    scala = models.CharField(max_length=20)
    rust = models.CharField(max_length=20)
    kotlin = models.CharField(max_length=20)
    swift = models.CharField(max_length=20)
    shell = models.CharField(max_length=20)
    date = models.DateField()


class CountCommit(models.Model):
    javascript = models.CharField(max_length=20)
    java = models.CharField(max_length=20)
    python = models.CharField(max_length=20)
    c = models.CharField(max_length=20)
    csharp = models.CharField(max_length=20)
    cplus = models.CharField(max_length=20)
    go = models.CharField(max_length=20)
    ruby = models.CharField(max_length=20)
    typescript = models.CharField(max_length=20)
    php = models.CharField(max_length=20)
    scala = models.CharField(max_length=20)
    rust = models.CharField(max_length=20)
    kotlin = models.CharField(max_length=20)
    swift = models.CharField(max_length=20)
    shell = models.CharField(max_length=20)
    date = models.DateField()


class CountRepository(models.Model):
    javascript = models.CharField(max_length=20)
    java = models.CharField(max_length=20)
    python = models.CharField(max_length=20)
    c = models.CharField(max_length=20)
    csharp = models.CharField(max_length=20)
    cplus = models.CharField(max_length=20)
    go = models.CharField(max_length=20)
    ruby = models.CharField(max_length=20)
    typescript = models.CharField(max_length=20)
    php = models.CharField(max_length=20)
    scala = models.CharField(max_length=20)
    rust = models.CharField(max_length=20)
    kotlin = models.CharField(max_length=20)
    swift = models.CharField(max_length=20)
    shell = models.CharField(max_length=20)
    date = models.DateField()

