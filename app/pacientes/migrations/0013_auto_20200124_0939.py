# Generated by Django 3.0.2 on 2020-01-24 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0012_paciente_actividad_fisica'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='foto_inicial',
            field=models.ImageField(blank=True, null=True, upload_to='fotos_pacientes/'),
        ),
    ]