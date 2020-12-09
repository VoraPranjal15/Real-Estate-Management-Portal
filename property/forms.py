
from django.forms import Select, fields
from django.forms import widgets
from django.forms.widgets import SelectMultiple
from .models import *
from django import forms



class PropertyForm(forms.ModelForm):
    type_house = forms.ChoiceField(choices=HOUSE_TYPES, widget=forms.Select)

    class Meta:
        model = Property
        fields = ['type_house','state','city','area','no_of_bedrooms',
        'no_of_floors','age_of_house','price','name','address','Description',
        'Parking','Gym','Conference_room','swimming_pool','plan','possession'
        ]
        widgets = {
            'Description':forms.Textarea,
            'address':forms.Textarea
        }

class PropertyImagesForm(forms.ModelForm):
    class Meta:
        model = PropertyImages
        fields=['Area_of_bedroom1','Bedroom1_Image','Area_of_bedroom2','Bedroom2_Image','Area_of_bedroom3','Bedroom3_Image','LivingRoom_Image','Area_of_livingroom','Kitchen_Image','Area_of_kitchen','Main_Image']

class PropertySpecsForm(forms.ModelForm):
    class Meta:
        model = property_specs
        fields=['kitchen_flooring','livingroom_flooring','electrical_Fitting','water_fitting','door_fitting','exterior_material','interior_material']

class Location_DetailsForm(forms.ModelForm):
    class Meta:
        model = Location
        fields=['nearby_hospital','nearby_school','nearby_ATM','nearby_mall','nearby_bank','nearby_grocery_shop']