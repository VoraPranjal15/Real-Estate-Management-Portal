# Generated by Django 3.1 on 2020-10-16 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_house', models.CharField(choices=[('penthouse', 'penthouse'), ('villa', 'villa'), ('bungalow', 'bungalow'), ('flat', 'flat')], default='penthouse', max_length=20)),
                ('state', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=20)),
                ('area', models.FloatField(default=False)),
                ('no_of_bedrooms', models.IntegerField(default=False)),
                ('no_of_floors', models.IntegerField(default=False)),
                ('age_of_house', models.IntegerField(default=True)),
                ('price', models.BigIntegerField(default=False)),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=100)),
                ('Parking', models.BooleanField(default=False)),
                ('Gym', models.BooleanField(default=False)),
                ('Conference_room', models.BooleanField(default=False)),
                ('swimming_pool', models.BooleanField(default=False)),
                ('plan', models.ImageField(null=True, upload_to='plans/')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('property_id', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='property.property')),
                ('nearby_hospital', models.CharField(max_length=20)),
                ('nearby_school', models.CharField(max_length=20)),
                ('nearby_ATM', models.CharField(max_length=20)),
                ('nearby_mall', models.CharField(max_length=20)),
                ('nearby_bank', models.CharField(max_length=20)),
                ('nearby_grocery_shop', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='property_specs',
            fields=[
                ('property_id', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='property.property')),
                ('kitchen_flooring', models.CharField(max_length=20)),
                ('livingroom_flooring', models.CharField(max_length=20)),
                ('electrical_Fitting', models.CharField(max_length=20)),
                ('water_fitting', models.CharField(max_length=20)),
                ('door_fitting', models.CharField(max_length=20)),
                ('exterior_material', models.CharField(max_length=20)),
                ('interior_material', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='Images/', verbose_name='Image')),
                ('property_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='property.property')),
            ],
        ),
    ]
