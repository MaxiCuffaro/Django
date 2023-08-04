# Generated by Django 4.2.1 on 2023-08-02 19:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0011_hobbies'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddIndex(
            model_name='relationship',
            index=models.Index(fields=['from_user', 'to_user'], name='base_relati_from_us_ec4811_idx'),
        ),
    ]