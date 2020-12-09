from property.choices import room_choices,price_choices,floor_choices,state_choices,type_house_choices
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.http import request

from django.http import response
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth.forms import AuthenticationForm

from ..forms import BuilderForm, BuyerSignUpForm
from ..models import  Builder, Builder, User


class BuyerSignUpView(CreateView):
    model = User
    form_class = BuyerSignUpForm
    user = User(is_buyer=True)
    template_name = 'registration/signup_form.html'
    

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'buyer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/b_login')



def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)#InBulit Login
                context ={
                    'room_choices':room_choices,
                    'price_choices':price_choices,
                    'floor_choices':floor_choices,
                    'state_choices':state_choices,
                    'type_house_choices':type_house_choices 
                }
                request.session['buyer_email']=user.email
                request.session['buyer_name']=user.name
                print(user.email)
                return render(request,'./Filter/mainpage.html',context)
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    
                return render(request, '../templates/registration/login.html',context={'form':AuthenticationForm()})
    else:
        return render(request, '../templates/registration/login.html',context={'form':AuthenticationForm()})


def logout_request(request):
    logout(request)    
    return render(request, '../templates/registration/signup.html')


