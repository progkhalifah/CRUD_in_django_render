from django.contrib.auth.models import User
from django.db import models


class Employees(models.Model):
    name = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=100, null=True)
    address = models.TextField(max_length=255, null=True)
    phone = models.IntegerField(null=True)

    def __str__(self):
        return self.name

