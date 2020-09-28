# Generated by Django 3.1.1 on 2020-09-28 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Especialidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especialidade', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crm', models.IntegerField(unique=True)),
                ('nome', models.CharField(max_length=150)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('telefone', models.IntegerField(blank=True, null=True, unique=True)),
                ('especialidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicos.especialidade')),
            ],
        ),
    ]
