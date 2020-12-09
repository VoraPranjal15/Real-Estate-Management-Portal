from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.db.models import fields
from django.forms.utils import ValidationError
from django.db import IntegrityError
from .models import Builder, Buyer,Seller ,User
from django.contrib.auth import get_user_model


class BuyerSignUpForm(UserCreationForm):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    age = forms.IntegerField()

   
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_buyer = True
        user.name = self.cleaned_data.get('name')
        user.email = self.cleaned_data.get('email')
        user.save()
        buyer = Buyer.objects.create(user=user)
        buyer.age = self.cleaned_data.get('age')
        buyer.save()
        return user


class SellerSignUpForm(UserCreationForm):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    contact = forms.CharField(max_length=100, required=True)
    city = forms.CharField(required = True)
    state = forms.CharField(required = True)

    User = get_user_model()    
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_seller = True
        user.name = self.cleaned_data.get('name')
        user.email = self.cleaned_data.get('email')
        user.save()
        seller= Seller.objects.create(user=user)
        seller.contact = self.cleaned_data.get('contact')
        seller.city = self.cleaned_data.get('city')
        seller.state = self.cleaned_data.get('state')
        seller.save()   
        return (user,seller)


class BuilderForm(forms.ModelForm):

    class Meta():
        model= Builder
        exclude = ['seller']

   

              




    