# Generated by Django 3.1 on 2020-11-07 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_auto_20201106_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='Description',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='property',
            name='address',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='property',
            name='city',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='property',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='property',
            name='state',
            field=models.CharField(max_length=30),
        ),
    ]
