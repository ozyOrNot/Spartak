# Generated by Django 4.1.3 on 2022-12-08 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_sportsman_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anthropometry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
                ('index', models.FloatField()),
                ('time', models.DateField()),
                ('sportman', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.sportsman')),
            ],
        ),
    ]
