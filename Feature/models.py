from django.db import models

# Create your models here.
from Namespace.models import Namespace


class Feature(models.Model):
    namespace = models.ForeignKey(Namespace, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)

    class Meta:
        managed = True
        db_table = 'feature'
        unique_together = (('namespace', 'name'),)

    def __str__(self):
        return self.name
