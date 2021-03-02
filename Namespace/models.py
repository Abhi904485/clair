from django.db import models


# Create your models here.

class Namespace(models.Model):
    name = models.CharField(verbose_name="Namespace Name", unique=True, max_length=128, blank=True, null=True)
    version_format = models.CharField(verbose_name="Namespace Version Format", max_length=128, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'namespace'

    def __str__(self):
        return self.name
