# Generated by Django 5.0.6 on 2024-11-11 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0010_delete_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='produtos',
            name='estoque',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
