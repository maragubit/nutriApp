# Generated by Django 3.0.2 on 2020-01-23 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mediciones', '0006_remove_medicion_perimetro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicion',
            name='altura',
        ),
    ]
