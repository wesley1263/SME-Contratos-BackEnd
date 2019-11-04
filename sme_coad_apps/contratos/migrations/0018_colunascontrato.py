# Generated by Django 2.2.4 on 2019-11-04 20:28

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contratos', '0017_auto_20191031_0804'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColunasContrato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('alterado_em', models.DateTimeField(auto_now=True, verbose_name='Alterado em')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('colunas_array', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=[{'field': 'termo_contrato', 'header': 'TC'}, {'field': 'processo', 'header': 'Processo'}, {'field': 'tipo_servico.nome', 'header': 'Tipode de Serviço'}, {'field': 'empresa_contratada.nome', 'header': 'Empresa'}, {'field': 'estado_contrato', 'header': 'Estado do Contrato'}, {'field': 'data_encerramento', 'header': 'Data Encerramento'}], verbose_name='Lista de campos')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='usuario_servidor', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Colunas do Usuário',
                'verbose_name_plural': 'Colunas do Usuário',
            },
        ),
    ]
