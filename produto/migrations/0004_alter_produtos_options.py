# Generated by Django 5.0.6 on 2024-07-20 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0003_alter_produtos_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='produtos',
            options={'ordering': ('-id',)},
        ),
    ]