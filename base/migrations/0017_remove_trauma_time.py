# Generated by Django 4.1.3 on 2022-12-14 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_trauma_sportman_alter_trauma_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trauma',
            name='time',
        ),
    ]
