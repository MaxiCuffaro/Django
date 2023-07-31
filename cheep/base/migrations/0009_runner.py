# Generated by Django 4.2.1 on 2023-07-31 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_comment_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Runner',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('medal', models.CharField(blank=True, choices=[('GOLD', 'Gold'), ('SILVER', 'Silver'), ('BRONZE', 'Bronze')], max_length=10)),
            ],
        ),
    ]
