# Generated by Django 4.1.3 on 2022-12-10 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_career_alter_anthropometry_height_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='career',
            name='sportman',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.sportsman'),
        ),
    ]
