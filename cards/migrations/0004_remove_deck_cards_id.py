# Generated by Django 4.1.4 on 2022-12-21 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0003_deck_cards_id_remove_deck_id_deck_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deck',
            name='cards_id',
        ),
    ]
