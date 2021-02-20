from django.db import models


# Create your models here.

class Namespace(models.Model):
    name = models.CharField(unique=True, max_length=128, blank=True, null=True)
    version_format = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'namespace'

    def __str__(self):
        return self.name
