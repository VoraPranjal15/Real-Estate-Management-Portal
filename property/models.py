from users.models import Seller
from django.db import models


HOUSE_TYPES = (
    ('penthouse','penthouse'),
    ('villa', 'villa'),
    ('bungalow','bungalow'),
)

 
class Property(models.Model):
    type_house = models.CharField(choices=HOUSE_TYPES,max_length=20, default='penthouse')
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    area = models.FloatField(blank=False, default = False)
    no_of_bedrooms = models.IntegerField(default = False)
    no_of_floors = models.IntegerField(default = False)
    age_of_house = models.IntegerField(default=True)
    price = models.BigIntegerField(default = False)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=1000)
    possession=models.CharField(max_length=30,default=False,null=True)
    Description = models.CharField(max_length=1000)
    Parking = models.BooleanField(default=False)
    Gym = models.BooleanField(default=False)
    Conference_room = models.BooleanField(default=False)
    swimming_pool = models.BooleanField(default=False)
    plan = models.ImageField(upload_to ='plans/' ,null=True)
    property_seller = models.ForeignKey(Seller,on_delete=models.CASCADE,blank=False,default=None)

class PropertyImages(models.Model):
    property_fk = models.ForeignKey(Property ,on_delete=models.CASCADE)
    Area_of_bedroom1 = models.IntegerField(default=0)
    Bedroom1_Image=models.ImageField(upload_to='images1/',null=False,default=False)
    Area_of_bedroom2=models.IntegerField(default=0,blank=True)
    Bedroom2_Image=models.ImageField(upload_to='images1/',null=True,default=False,blank=True)
    Area_of_bedroom3=models.IntegerField(default=0,blank=True)
    Bedroom3_Image=models.ImageField(upload_to='images1/',null=True,default=False,blank=True)
    LivingRoom_Image=models.ImageField(upload_to='images1/',null=False,default=False,blank=False)
    Area_of_livingroom=models.IntegerField(default=0,blank=True)
    Kitchen_Image=models.ImageField(upload_to='images1/',null=False,default=False,blank=False)
    Area_of_kitchen=models.IntegerField(default=0,blank=True)
    Main_Image = models.ImageField(upload_to='images1/',blank=True,default=False,null=False)


    

#How to show composition with Property model    
#Must be shown in property Form but stored in different table
#How to put a Foriegnkey property_id
class property_specs(models.Model):
    property_id =  models.OneToOneField(Property,on_delete=models.CASCADE,default=None,primary_key=True) 
    kitchen_flooring = models.CharField(max_length = 20)
    livingroom_flooring = models.CharField(max_length = 20)
    electrical_Fitting = models.CharField(max_length = 20)
    water_fitting = models.CharField(max_length=20)
    door_fitting = models.CharField(max_length=20)
    exterior_material = models.CharField(max_length=20)
    interior_material = models.CharField(max_length=20)

#How to show aggregation with Property model
#Must be shown in property Form but stored in different table
#How to put a Foriegnkey property_id
class Location(models.Model):
    property_id = models.OneToOneField(Property,on_delete=models.CASCADE,default=None,primary_key=True)
    nearby_hospital = models.CharField(max_length=20)
    nearby_school = models.CharField(max_length=20)
    nearby_ATM = models.CharField(max_length=20)
    nearby_mall = models.CharField(max_length=20)
    nearby_bank = models.CharField(max_length=20)
    nearby_grocery_shop = models.CharField(max_length=20)


