# Generated by Django 3.1.7 on 2021-04-07 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menuapp', '0002_auto_20210326_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plato',
            name='ingredientes',
            field=models.ManyToManyField(blank=True, to='menuapp.Ingrediente'),
        ),
    ]