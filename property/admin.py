from .models import Property, PropertyImages,property_specs,Location
from django.contrib import admin

admin.site.register(Property)
admin.site.register(PropertyImages)
admin.site.register(property_specs)
admin.site.register(Location)