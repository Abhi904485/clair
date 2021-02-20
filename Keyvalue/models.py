from django.db import models


# Create your models here.

class Keyvalue(models.Model):
    key = models.CharField(unique=True, max_length=128)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'keyvalue'

    def __str__(self):
        return self.key + "       " + self.value
