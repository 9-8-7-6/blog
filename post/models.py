from django.db import models
from datetime import datetime

class Post(models.Model):
    title = models.CharField(max_length=150)
    body = models.CharField(max_length=1000)
    created_at = models.DateTimeField(default = datetime.now, blank = True)
