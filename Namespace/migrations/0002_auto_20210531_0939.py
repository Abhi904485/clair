# Generated by Django 3.1.7 on 2021-05-31 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Namespace', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='namespace',
            name='name',
            field=models.CharField(blank=True, max_length=128, null=True, unique=True, verbose_name='Namespace Name'),
        ),
        migrations.AlterField(
            model_name='namespace',
            name='version_format',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Namespace Version Format'),
        ),
    ]
