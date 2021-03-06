# Generated by Django 3.1.7 on 2021-03-26 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoDePlato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, unique=True)),
                ('publicacion', models.DateTimeField(verbose_name='Dia publicado')),
                ('precio', models.IntegerField(default=0)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='menuapp.tipodeplato')),
            ],
        ),
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, unique=True)),
                ('plato', models.ManyToManyField(to='menuapp.Plato')),
            ],
        ),
    ]
