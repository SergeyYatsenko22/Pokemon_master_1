# Generated by Django 3.1.14 on 2023-03-02 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0018_remove_pokemon_next_evolution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='image',
            field=models.ImageField(blank=True, default='pokemon_images/No.jpg', null=True, upload_to='pokemon_images'),
        ),
    ]
