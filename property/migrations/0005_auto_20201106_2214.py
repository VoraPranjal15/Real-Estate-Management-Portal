# Generated by Django 3.1 on 2020-11-06 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_propertyimages_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propertyimages',
            name='category',
        ),
        migrations.RemoveField(
            model_name='propertyimages',
            name='image',
        ),
        migrations.AddField(
            model_name='property',
            name='possession',
            field=models.CharField(default=False, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='propertyimages',
            name='Area_of_bedroom1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='propertyimages',
            name='Area_of_bedroom2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='propertyimages',
            name='Area_of_bedroom3',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='propertyimages',
            name='Area_of_kitchen',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='propertyimages',
            name='Area_of_livingroom',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='propertyimages',
            name='Bedroom1_Image',
            field=models.ImageField(default=False, upload_to='images1/'),
        ),
        migrations.AddField(
            model_name='propertyimages',
            name='Bedroom2_Image',
            field=models.ImageField(default=False, null=True, upload_to='images1/'),
        ),
        migrations.AddField(
            model_name='propertyimages',
            name='Bedroom3_Image',
            field=models.ImageField(default=False, null=True, upload_to='images1/'),
        ),
        migrations.AddField(
            model_name='propertyimages',
            name='Kitchen_Image',
            field=models.ImageField(default=False, null=True, upload_to='images1/'),
        ),
        migrations.AddField(
            model_name='propertyimages',
            name='LivingRoom_Image',
            field=models.ImageField(default=False, null=True, upload_to='images1/'),
        ),
        migrations.AlterField(
            model_name='propertyimages',
            name='property_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.property'),
        ),
    ]