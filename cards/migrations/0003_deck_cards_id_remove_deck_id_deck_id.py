# Generated by Django 4.1.4 on 2022-12-21 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_rename_decklist_card'),
    ]

    operations = [
        migrations.AddField(
            model_name='deck',
            name='cards_id',
            field=models.ManyToManyField(to='cards.card'),
        ),
        migrations.RemoveField(
            model_name='deck',
            name='id',
        ),
        migrations.AddField(
            model_name='deck',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
