# Generated by Django 4.2.1 on 2023-08-03 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_profile_followers_and_more'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='relationship',
            name='base_relati_from_us_ec4811_idx',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='followers',
        ),
    ]
