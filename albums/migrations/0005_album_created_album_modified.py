# Generated by Django 4.1.2 on 2022-10-18 14:03

from django.db import migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0004_rename_is_explicit_album_is_approved_by_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='created',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created'),
        ),
        migrations.AddField(
            model_name='album',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified'),
        ),
    ]