from django.db import models

# Create your models here.


class Name(models.Model):
    name = models.TextField()
    amount = models.IntegerField()
