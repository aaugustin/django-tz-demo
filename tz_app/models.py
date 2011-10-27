from django.db import models

class Name(models.Model):
    name = models.CharField(max_length=32, unique=True)
    dated = models.DateTimeField()

class AutoName(models.Model):
    name = models.CharField(max_length=32, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
