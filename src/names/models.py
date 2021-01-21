from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.TextField(max_length=100)
    amount = models.IntegerField()


class UploadJsonFile(models.Model):
    data = models.JSONField(default='')
