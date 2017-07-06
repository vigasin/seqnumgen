from django.db import models


class Tag(models.Model):
    name = models.CharField(unique=True, max_length=1024)
    num = models.IntegerField(default=0)
