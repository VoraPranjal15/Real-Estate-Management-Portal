# Generated by Django 3.1 on 2020-11-07 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_propertyimages_main_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertyimages',
            name='Main_Image',
            field=models.ImageField(blank=True, default=False, upload_to='images1/'),
        ),
    ]
