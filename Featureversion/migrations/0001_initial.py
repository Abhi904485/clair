# Generated by Django 3.1 on 2021-02-17 20:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Feature', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Featureversion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=128)),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Feature.feature')),
            ],
            options={
                'db_table': 'featureversion',
                'managed': True,
                'unique_together': {('feature', 'version')},
            },
        ),
    ]
