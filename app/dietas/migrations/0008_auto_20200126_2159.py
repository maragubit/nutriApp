# Generated by Django 3.0.2 on 2020-01-26 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dietas', '0007_auto_20200124_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dieta',
            name='nombre',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
