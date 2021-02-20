from django.db import models


# Create your models here.

class SchemaMigrations(models.Model):
    version = models.IntegerField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'schema_migrations'

    def __str__(self):
        return str(self.version)
