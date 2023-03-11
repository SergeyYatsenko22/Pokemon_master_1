# Generated by Django 3.1.14 on 2023-02-28 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0016_auto_20230228_1953'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemon',
            old_name='next_evolutions',
            new_name='next_evolution',
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='previous_evolution',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='next_evolutions', to='pokemon_entities.pokemon'),
        ),
    ]
