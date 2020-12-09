from property.models import PropertyImages
from property.models import Property
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Avg, Count
from django.forms import inlineformset_factory
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.http import  response
from django.http import request
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.base import ContextMixin


from ..forms import BuilderForm, SellerSignUpForm
from ..models import Builder, User , Seller
import urllib

class SellerSignUpView(CreateView):
    model = User
    form_class = SellerSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'seller'
        return super().get_context_data(**kwargs)

    def form_valid(self,form):
        user,seller = form.save()
        #login(self.request, user)
        print(seller)
        self.request.session['seller']=seller.user.id
        url = 'registration/login/'
        return redirect(url)
        # context={'seller':seller,'form':BuilderForm()}
        # return render(self.request,'../templates/registration/details.html',context)
       
def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                print(request)
                request.user = user
                s = Seller.objects.get(user=user)
                request.session['seller_pk'] = s.pk
                seller_obj = Seller.objects.get(pk=request.session['seller_pk'])
                #request.session['seller_object']=seller_obj
                #seller_property = Property.objects.get(property_seller=seller_obj)
                seller_property = Property.objects.filter(property_seller=seller_obj)
                images = PropertyImages.objects.all()
                return render(request,'./Hello.html',{'properties':seller_property,'images':images})
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    
                return render(request, '../templates/registration/login.html',context={'form':AuthenticationForm()})
    else:
        if request.user.is_authenticated:
            s = Seller.objects.get(user=request.user)
            request.session['seller_pk'] = s.pk
            seller_obj = Seller.objects.get(pk=request.session['seller_pk'])
            seller_property = Property.objects.filter(property_seller=seller_obj)
            images = PropertyImages.objects.all()
            return render(request,'./Hello.html',{'properties':seller_property,'images':images})
        else:
            return render(request, '../templates/registration/login.html',context={'form':AuthenticationForm()})
    

def logout_request(request):
    logout(request)    
    return render(request, '../templates/registration/signup.html')

      