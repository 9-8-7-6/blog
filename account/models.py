from django.db import models


class account(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)