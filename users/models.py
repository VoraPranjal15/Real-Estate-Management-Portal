from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe
from django.contrib.auth import get_user_model


class User(AbstractUser):
    is_buyer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    name = models.CharField(max_length=100,null= False,blank=False)
    email = models.EmailField(null=False,blank=False) 

User = get_user_model()
class Buyer(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE,primary_key=True)
    age = models.IntegerField(default=0,blank=True)


    def __str__(self):
        return self.user.name

    
#User = get_user_model()    
class Seller(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE,primary_key=True)
    contact = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length =100)
    buyers = models.ManyToManyField(Buyer,related_name='buyers')

    def __str__(self):
        return self.user.name

  
  

   
class Builder(models.Model):
    seller = models.OneToOneField(Seller,on_delete=models.CASCADE,primary_key=True,default=None)
    landmark_projects = models.CharField(max_length=100) #Multiple comma seperated strings here
    current_projects = models.CharField(max_length=100) #Multiple comma seperated strings here
    Rera_Certificate = models.FileField(upload_to='certificates/',null=False)
    lawyer = models.CharField(max_length=20)
    architect = models.CharField(max_length=20)
    chartered_acc = models.CharField(max_length=20)
    site_incharge = models.CharField(max_length=20)
    sales_team_rep = models.CharField(max_length=20)
    project_duration = models.FloatField(default=False)
    Youtube_channel=models.CharField(max_length=100,default=None,null=True)
    facebook_handle=models.CharField(max_length=100,default=None,null=True)
    Twitter_handle=models.CharField(max_length=100,default=None,null=True)
    bank_tie_ups = models.CharField(max_length=100) #Multiple comma seperated strings here
    Embed_link=models.CharField(max_length=1000,default=None,null=True,blank=True)


