# Generated by Django 5.0.6 on 2024-08-05 00:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fabrica', '0001_initial'),
        ('produto', '0006_produtos_mostrar'),
    ]

    operations = [
        migrations.AddField(
            model_name='produtos',
            name='fabrica',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fabrica.fabrica'),
        ),
    ]