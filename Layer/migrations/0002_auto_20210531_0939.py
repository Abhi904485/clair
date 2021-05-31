# Generated by Django 3.1.7 on 2021-05-31 09:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Namespace', '0002_auto_20210531_0939'),
        ('Layer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='layer',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Layer Created At'),
        ),
        migrations.AlterField(
            model_name='layer',
            name='engineversion',
            field=models.SmallIntegerField(verbose_name='Layer Engine Version'),
        ),
        migrations.AlterField(
            model_name='layer',
            name='name',
            field=models.CharField(max_length=128, unique=True, verbose_name='Layer Name'),
        ),
        migrations.AlterField(
            model_name='layer',
            name='namespace',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Namespace.namespace', verbose_name='Layer Namespace'),
        ),
        migrations.AlterField(
            model_name='layer',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Layer.layer', verbose_name='Layer Parent'),
        ),
    ]
