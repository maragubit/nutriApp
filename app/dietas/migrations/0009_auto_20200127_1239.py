# Generated by Django 3.0.2 on 2020-01-27 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dietas', '0008_auto_20200126_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='plato',
            name='desayuno',
            field=models.CharField(choices=[('SI', 'sí'), ('NO', 'no')], default='NO', max_length=5),
        ),
        migrations.AddField(
            model_name='plato',
            name='media_manana',
            field=models.CharField(choices=[('SI', 'sí'), ('NO', 'no')], default='NO', max_length=5),
        ),
        migrations.AddField(
            model_name='plato',
            name='postre',
            field=models.CharField(choices=[('SI', 'sí'), ('NO', 'no')], default='NO', max_length=5),
        ),
    ]
