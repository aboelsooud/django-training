# Generated by Django 4.1.2 on 2022-10-23 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0015_alter_song_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
