# Generated by Django 3.1.14 on 2023-03-02 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0029_auto_20230302_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='lat',
            field=models.FloatField(null=True, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='lon',
            field=models.FloatField(null=True, verbose_name='Долгота'),
        ),
    ]
