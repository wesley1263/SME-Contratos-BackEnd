# Generated by Django 2.2.4 on 2019-11-17 03:00

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('contratos', '0029_auto_20191116_2356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contrato',
            name='nucleo',
        ),
    ]