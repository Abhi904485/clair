from django.db import models

# Create your models here.
from Namespace.models import Namespace


class Layer(models.Model):
    name = models.CharField(verbose_name="Layer Name", unique=True, max_length=128)
    engineversion = models.SmallIntegerField(verbose_name="Layer Engine Version")
    parent = models.ForeignKey('self', verbose_name="Layer Parent", on_delete=models.CASCADE, blank=True, null=True)
    namespace = models.ForeignKey(Namespace, verbose_name="Layer Namespace", on_delete=models.CASCADE, blank=True,
                                  null=True)
    created_at = models.DateTimeField(verbose_name="Layer Created At", blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'layer'

    def __str__(self):
        return self.name
