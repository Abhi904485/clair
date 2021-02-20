from django.db import models

# Create your models here.
from Namespace.models import Namespace


class Layer(models.Model):
    name = models.CharField(unique=True, max_length=128)
    engineversion = models.SmallIntegerField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    namespace = models.ForeignKey(Namespace, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'layer'

    def __str__(self):
        return self.name
