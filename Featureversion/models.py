from django.db import models

# Create your models here.
from Feature.models import Feature


class Featureversion(models.Model):
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)
    version = models.CharField(verbose_name="Feature Version", max_length=128)

    class Meta:
        managed = True
        db_table = 'featureversion'
        unique_together = (('feature', 'version'),)

    def __str__(self):
        return self.version
