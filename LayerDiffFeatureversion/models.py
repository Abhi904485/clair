from django.db import models

# Create your models here.
from Featureversion.models import Featureversion
from Layer.models import Layer


class LayerDiffFeatureversion(models.Model):
    layer = models.ForeignKey(Layer, on_delete=models.CASCADE)
    featureversion = models.ForeignKey(Featureversion, on_delete=models.CASCADE)
    modification = models.TextField()  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'layer_diff_featureversion'
        unique_together = (('layer', 'featureversion'),)

    def __str__(self):
        return self.featureversion.version
