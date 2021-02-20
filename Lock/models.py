from django.db import models


# Create your models here.

class Lock(models.Model):
    name = models.CharField(unique=True, max_length=64)
    owner = models.CharField(max_length=64)
    until = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'lock'
