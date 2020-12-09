from django.urls import include, path
from . import views1

urlpatterns = [
    path('form/',views1.new_user,name='new_thread'),
]


