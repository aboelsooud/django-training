# Generated by Django 4.1.2 on 2022-10-14 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0002_album_is_explict_alter_album_cost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='is_explict',
            new_name='is_explicit',
        ),
    ]