# Generated by Django 2.2.4 on 2019-12-02 17:44

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contratos', '0003_remove_contratounidade_dre_lote'),
    ]

    operations = [
        migrations.CreateModel(
            name='FiscaisUnidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('alterado_em', models.DateTimeField(auto_now=True, verbose_name='Alterado em')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('tipo_fiscal',
                 models.CharField(choices=[('TITULAR', 'Titular'), ('SUPLENTE', 'Suplente')], default='SUPLENTE',
                                  max_length=15)),
                ('contrato_unidade',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fiscais',
                                   to='contratos.ContratoUnidade')),
                ('fiscal',
                 models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='contratos_fiscalizados',
                                   to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Fiscal da Unidade de Contrato',
                'verbose_name_plural': 'Fiscais das Unidades de Contratos',
            },
        ),
    ]
