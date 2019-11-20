# Generated by Django 2.2.4 on 2019-11-19 19:09

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('contratos', '0032_merge_20191119_1203'),
    ]

    operations = [
        migrations.CreateModel(
            name='ObrigacaoContratual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('alterado_em', models.DateTimeField(auto_now=True, verbose_name='Alterado em')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('item', models.CharField(max_length=15)),
                ('obrigacao', models.TextField(default='')),
                ('contrato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='obrigacao_contratual', to='contratos.Contrato')),
            ],
            options={
                'verbose_name': 'Obrigação Contratual',
                'verbose_name_plural': 'Obrigações Contratuais',
            },
        ),
    ]
