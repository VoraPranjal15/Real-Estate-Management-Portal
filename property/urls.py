from django.http import request
from django.urls import include, path
from . import views

urlpatterns = [
    path('create_property/',views.save_property,name='property_create'),
    path('property_images/',views.save_property_images,name='property_images'),
    path('property_specs/',views.save_property_specs,name='property_specs'),
    path('property_location/',views.save_location,name='location_details'),
    path('property_filter/',views.search,name='filter_property'),
    path('renderproperty_filter/',views.renderfilterback,name='renderfilter_propertyonback'),
    path('property_detail/<str:id>/',views.property_detail,name='property_details'),
    path('sellerproperty_detail/<str:id>/',views.sellerproperty_detail,name='sellerproperty_details'),
    path('compare/',views.compareview,name='compareview'),
    path('rendercompareview/',views.rendercompareview,name='rendercompareview'),
    path('sendmail/<str:emailid>/<str:pname>/',views.send_email,name='email'),
    path('takevisit/<str:emailid>/<str:pname>/',views.take_visit,name='takevisit'),
    path('back',views.back,name='back')
]