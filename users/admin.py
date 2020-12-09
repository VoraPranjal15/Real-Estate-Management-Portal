from django.contrib import admin
from .models import Buyer, Seller, User,Builder

admin.site.register(Buyer)
admin.site.register(Seller)
admin.site.register(User)
admin.site.register(Builder)

