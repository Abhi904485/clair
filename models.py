# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
# #   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.
# from django.db import models
#
#
# class Namespace(models.Model):
#     name = models.CharField(unique=True, max_length=128, blank=True, null=True)
#     version_format = models.CharField(max_length=128, blank=True, null=True)
#
#     class Meta:
#         managed = True
#         db_table = 'namespace'
#
#
# class Feature(models.Model):
#     namespace = models.ForeignKey(Namespace, on_delete=models.CASCADE)
#     name = models.CharField(max_length=128)
#
#     class Meta:
#         managed = True
#         db_table = 'feature'
#         unique_together = (('namespace', 'name'),)
#
#
# class Featureversion(models.Model):
#     feature = models.ForeignKey(Feature, on_delete=models.CASCADE)
#     version = models.CharField(max_length=128)
#
#     class Meta:
#         managed = True
#         db_table = 'featureversion'
#         unique_together = (('feature', 'version'),)
#
#
# class Keyvalue(models.Model):
#     key = models.CharField(unique=True, max_length=128)
#     value = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = True
#         db_table = 'keyvalue'
#
#
# class Layer(models.Model):
#     name = models.CharField(unique=True, max_length=128)
#     engineversion = models.SmallIntegerField()
#     parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
#     namespace = models.ForeignKey(Namespace, on_delete=models.CASCADE, blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = True
#         db_table = 'layer'
#
#
# class LayerDiffFeatureversion(models.Model):
#     layer = models.ForeignKey(Layer, on_delete=models.CASCADE)
#     featureversion = models.ForeignKey(Featureversion, on_delete=models.CASCADE)
#     modification = models.TextField()  # This field type is a guess.
#
#     class Meta:
#         managed = True
#         db_table = 'layer_diff_featureversion'
#         unique_together = (('layer', 'featureversion'),)
#
#
# class Lock(models.Model):
#     name = models.CharField(unique=True, max_length=64)
#     owner = models.CharField(max_length=64)
#     until = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = True
#         db_table = 'lock'
#
#
# class SchemaMigrations(models.Model):
#     version = models.IntegerField(primary_key=True)
#
#     class Meta:
#         managed = True
#         db_table = 'schema_migrations'
#
#
# class Vulnerability(models.Model):
#     namespace = models.ForeignKey(Namespace, on_delete=models.CASCADE)
#     name = models.CharField(max_length=128)
#     description = models.TextField(blank=True, null=True)
#     link = models.CharField(max_length=128, blank=True, null=True)
#     severity = models.TextField()  # This field type is a guess.
#     metadata = models.TextField(blank=True, null=True)
#     created_at = models.DateTimeField(blank=True, null=True)
#     deleted_at = models.DateTimeField(blank=True, null=True)
#     severity_source = models.CharField(max_length=128, blank=True, null=True)
#
#     class Meta:
#         managed = True
#         db_table = 'vulnerability'
#
#
# class VulnerabilityFixedinFeature(models.Model):
#     vulnerability = models.ForeignKey(Vulnerability, on_delete=models.CASCADE)
#     feature = models.ForeignKey(Feature, on_delete=models.CASCADE)
#     version = models.CharField(max_length=128)
#
#     class Meta:
#         managed = True
#         db_table = 'vulnerability_fixedin_feature'
#         unique_together = (('vulnerability', 'feature'),)
#
#
# class VulnerabilityAffectsFeatureversion(models.Model):
#     vulnerability = models.ForeignKey(Vulnerability, on_delete=models.CASCADE)
#     featureversion = models.ForeignKey(Featureversion, on_delete=models.CASCADE)
#     fixedin = models.ForeignKey(VulnerabilityFixedinFeature, on_delete=models.CASCADE)
#
#     class Meta:
#         managed = True
#         db_table = 'vulnerability_affects_featureversion'
#         unique_together = (('vulnerability', 'featureversion'),)
#
#
# class VulnerabilityNotification(models.Model):
#     name = models.CharField(unique=True, max_length=64)
#     created_at = models.DateTimeField(blank=True, null=True)
#     notified_at = models.DateTimeField(blank=True, null=True)
#     deleted_at = models.DateTimeField(blank=True, null=True)
#     old_vulnerability = models.ForeignKey(Vulnerability, on_delete=models.CASCADE, blank=True, null=True)
#     new_vulnerability = models.ForeignKey(Vulnerability, on_delete=models.CASCADE, blank=True, null=True)
#
#     class Meta:
#         managed = True
#         db_table = 'vulnerability_notification'
