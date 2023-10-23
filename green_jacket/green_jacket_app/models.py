
from django.db.models import F, Sum, Case, When

from django.db import models

class Brand(models.Model):
    name    = models.CharField(max_length=50)
    score   = models.IntegerField()
