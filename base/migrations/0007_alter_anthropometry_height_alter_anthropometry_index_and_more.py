# Generated by Django 4.1.3 on 2022-12-08 23:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_anthropometry_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anthropometry',
            name='height',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='anthropometry',
            name='index',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='anthropometry',
            name='sportman',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.sportsman'),
        ),
        migrations.AlterField(
            model_name='anthropometry',
            name='weight',
            field=models.CharField(max_length=3),
        ),
    ]