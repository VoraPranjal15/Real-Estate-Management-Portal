# Generated by Django 3.1 on 2020-11-07 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_auto_20201107_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertyimages',
            name='Main_Image',
            field=models.ImageField(blank=True, default=False, upload_to='images1'),
        ),
    ]
