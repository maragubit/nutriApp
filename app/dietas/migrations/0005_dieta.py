# Generated by Django 3.0.2 on 2020-01-24 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dietas', '0004_auto_20200124_1413'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dieta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('desayuno1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='dietas.Plato')),
                ('desayuno2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='dietas.Plato')),
                ('desayuno3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='dietas.Plato')),
                ('dia1_almuerzo1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='dietas.Plato')),
                ('dia1_almuerzo2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='dietas.Plato')),
                ('dia1_cena1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='dietas.Plato')),
                ('dia1_cena2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='dietas.Plato')),
                ('dia1_media_manana', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='dietas.Plato')),
                ('dia1_merienda', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='dietas.Plato')),
                ('dia1_postre_almuerzo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='dietas.Plato')),
                ('dia1_postre_cena', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='dietas.Plato')),
                ('dia2_almuerzo1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='dietas.Plato')),
                ('dia2_almuerzo2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='dietas.Plato')),
                ('dia2_cena1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='dietas.Plato')),
                ('dia2_cena2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='dietas.Plato')),
                ('dia2_media_manana', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='dietas.Plato')),
                ('dia2_merienda', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='dietas.Plato')),
                ('dia2_postre_almuerzo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='dietas.Plato')),
                ('dia2_postre_cena', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='dietas.Plato')),
                ('dia3_almuerzo1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='dietas.Plato')),
                ('dia3_almuerzo2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='dietas.Plato')),
                ('dia3_cena1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='dietas.Plato')),
                ('dia3_cena2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='dietas.Plato')),
                ('dia3_media_manana', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='dietas.Plato')),
                ('dia3_merienda', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='dietas.Plato')),
                ('dia3_postre_almuerzo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='dietas.Plato')),
                ('dia3_postre_cena', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='dietas.Plato')),
            ],
        ),
    ]
