# Generated by Django 3.0.2 on 2020-01-21 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0004_paciente_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='historial',
            field=models.TextField(blank=True, null=True),
        ),
    ]
