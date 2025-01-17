# Generated by Django 3.0.2 on 2020-01-23 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0008_auto_20200123_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='foto_inicial',
            field=models.ImageField(blank=True, null=True, upload_to='fotos_pacientes'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='peso_inicial',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='peso_objetivo',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
    ]
