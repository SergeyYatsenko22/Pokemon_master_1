# Generated by Django 3.1.14 on 2023-03-02 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0026_auto_20230302_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='title',
            field=models.CharField(default='default', max_length=200, verbose_name='Имя покемона'),
            preserve_default=False,
        ),
    ]
