# Generated by Django 3.0.2 on 2020-01-23 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediciones', '0007_remove_medicion_altura'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicion',
            name='grasa_kg',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=2, null=True),
        ),
    ]
