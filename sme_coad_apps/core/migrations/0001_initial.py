# Generated by Django 2.2.4 on 2019-09-19 14:41

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Divisao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=160, verbose_name='Nome')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('alterado_em', models.DateTimeField(auto_now=True, verbose_name='Alterado em')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('sigla', models.CharField(max_length=15, verbose_name='Sigla')),
            ],
            options={
                'verbose_name': 'Divisão',
                'verbose_name_plural': 'Divisões',
            },
        ),
        migrations.CreateModel(
            name='Nucleo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=160, verbose_name='Nome')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('alterado_em', models.DateTimeField(auto_now=True, verbose_name='Alterado em')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('sigla', models.CharField(max_length=20, verbose_name='Sigla')),
                ('divisao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Divisao')),
            ],
            options={
                'verbose_name': 'Núcleo',
                'verbose_name_plural': 'Núcleos',
            },
        ),
    ]
