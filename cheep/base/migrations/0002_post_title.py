# Generated by Django 4.2.1 on 2023-07-24 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='TITULO', max_length=100),
            preserve_default=False,
        ),
    ]