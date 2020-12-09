# Generated by Django 3.1 on 2020-10-16 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('property', '0002_property_property_seller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='property_seller',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='users.seller'),
        ),
    ]
