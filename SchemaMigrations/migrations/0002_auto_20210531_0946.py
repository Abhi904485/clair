# Generated by Django 3.1.7 on 2021-05-31 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SchemaMigrations', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='schemamigrations',
            options={'managed': True, 'verbose_name_plural': 'schema_migrations'},
        ),
        migrations.AlterField(
            model_name='schemamigrations',
            name='version',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='Version'),
        ),
    ]
