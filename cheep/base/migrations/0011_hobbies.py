# Generated by Django 4.2.1 on 2023-07-31 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_delete_runner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hobbies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desde_cuando', models.DateField()),
                ('time_training', models.TimeField()),
            ],
        ),
    ]
