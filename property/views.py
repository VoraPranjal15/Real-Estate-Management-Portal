from smtplib import SMTPException
from users.models import Builder
import json
from django.db.models import query
from django.db.models.query import QuerySet
from django.forms import modelformset_factory
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .forms import Location_DetailsForm, PropertyForm, PropertyImagesForm, PropertySpecsForm
from django.http import JsonResponse
from .models import * 
from django.core.mail import send_mail
from django.core import serializers
import smtplib
from property.choices import room_choices,price_choices,floor_choices,state_choices,type_house_choices

def save_property(request):
    # ImageFormSet = modelformset_factory(PropertyImages,form = PropertyImagesForm, extra=5)

    if request.method == 'POST':

        propertyForm = PropertyForm(request.POST,request.FILES)
        # formset = ImageFormSet(request.POST, request.FILES, queryset = PropertyImages.objects.none())

        if propertyForm.is_valid():
            # property=propertyForm.save(commit=False)
            type_house = propertyForm.cleaned_data['type_house']
            state = propertyForm.cleaned_data['state']
            city = propertyForm.cleaned_data['city']
            area = propertyForm.cleaned_data['area']
            no_of_bedrooms = propertyForm.cleaned_data['no_of_bedrooms']
            no_of_floors =  propertyForm.cleaned_data['no_of_floors']
            age_of_house = propertyForm.cleaned_data['age_of_house']
            price = propertyForm.cleaned_data['price']
            name = propertyForm.cleaned_data['name']
            address = propertyForm.cleaned_data['address']
            Description = propertyForm.cleaned_data['Description']
            possession=propertyForm.cleaned_data['possession']
            Parking = propertyForm.cleaned_data['Parking']
            Gym = propertyForm.cleaned_data['Gym']
            Conference_room=propertyForm.cleaned_data['Conference_room']
            swimming_pool = propertyForm.cleaned_data['swimming_pool']
            plan = propertyForm.cleaned_data['plan']
            seller_obj = Seller.objects.get(pk=request.session['seller_pk'])
            property = Property(type_house=type_house,state=state,city=city,area=area,no_of_bedrooms=no_of_bedrooms,no_of_floors=no_of_floors,age_of_house=age_of_house,price=price,name=name,address=address,Description=Description,Parking=Parking,Gym=Gym,Conference_room=Conference_room,swimming_pool=swimming_pool,plan=plan,property_seller=seller_obj,possession=possession)
            property.save()
            request.session['property_id'] = property.id
            return redirect('property_images')
            # return redirect('property_specs')
        else:
          return render(request,'./Notfound.html')
    else:
       propertyForm = PropertyForm()
       return render(request,'./propertycreate.html',{'propertyForm':propertyForm})
    
def save_property_images(request):

    if request.method == 'POST':
        propertyimagesform = PropertyImagesForm(request.POST,request.FILES)

        if propertyimagesform.is_valid():
            area_bedroom1=propertyimagesform.cleaned_data['Area_of_bedroom1']
            image_bedroom1=propertyimagesform.cleaned_data['Bedroom1_Image']
            area_bedroom2=propertyimagesform.cleaned_data['Area_of_bedroom2']
            image_bedroom2=propertyimagesform.cleaned_data['Bedroom2_Image']
            area_bedroom3=propertyimagesform.cleaned_data['Area_of_bedroom3']
            image_bedroom3=propertyimagesform.cleaned_data['Bedroom3_Image']
            livingroom_image=propertyimagesform.cleaned_data['LivingRoom_Image']
            area_livingroom=propertyimagesform.cleaned_data['Area_of_livingroom']
            kitchen_image=propertyimagesform.cleaned_data['Kitchen_Image']
            area_kitchen=propertyimagesform.cleaned_data['Area_of_kitchen']
            main_image=propertyimagesform.cleaned_data['Main_Image']
            property = Property.objects.get(pk=request.session['property_id'])
            propertyimages=PropertyImages(Area_of_bedroom1=area_bedroom1,Bedroom1_Image=image_bedroom1,Area_of_bedroom2=area_bedroom2,Bedroom2_Image=image_bedroom2,Area_of_bedroom3=area_bedroom3,Bedroom3_Image=image_bedroom3,LivingRoom_Image=livingroom_image,Area_of_livingroom=area_livingroom,Kitchen_Image=kitchen_image,Area_of_kitchen=area_kitchen,Main_Image=main_image,property_fk=property)
            propertyimages.save()
            return redirect('property_specs')
        else:
            return render(request,'./Notfound.html')

    else:
        propertyimagesform=PropertyImagesForm()
        return render(request,'./propertyimages.html',{'propertyimagesform':propertyimagesform})
        


                

def save_property_specs(request):
    if request.method == 'POST':
        specs_form = PropertySpecsForm(request.POST)

        if specs_form.is_valid():
            kitchen_flooring = specs_form.cleaned_data['kitchen_flooring']
            livingroom_flooring = specs_form.cleaned_data['livingroom_flooring']
            electrical_Fitting = specs_form.cleaned_data['electrical_Fitting']
            water_fitting = specs_form.cleaned_data['water_fitting']
            door_fitting = specs_form.cleaned_data['door_fitting']
            exterior_material = specs_form.cleaned_data['exterior_material']
            interior_material = specs_form.cleaned_data['interior_material']
            property = Property.objects.get(pk=request.session['property_id'])
            specs = property_specs(property_id=property,kitchen_flooring=kitchen_flooring,livingroom_flooring=livingroom_flooring,electrical_Fitting=electrical_Fitting,water_fitting=water_fitting,door_fitting=door_fitting,exterior_material=exterior_material,interior_material=interior_material)
            specs.save()
            print(request.POST.get('property_id'))
            return redirect('location_details')
        else:
            return render(request,'./Notfound.html')
    
    else:
        property_specs_form = PropertySpecsForm()
        return render(request,'./propertyspecs.html',{'form':property_specs_form})

def save_location(request):
    if request.method=='POST':
        LocationForm = Location_DetailsForm(request.POST)

        if LocationForm.is_valid():
           NearByHospital = LocationForm.cleaned_data['nearby_hospital']
           NearBySchool=LocationForm.cleaned_data['nearby_school']
           NearByATM = LocationForm.cleaned_data['nearby_ATM']
           NearByBank = LocationForm.cleaned_data['nearby_bank']
           NearByMall = LocationForm.cleaned_data['nearby_mall']
           NearByGroceryShop = LocationForm.cleaned_data['nearby_grocery_shop']
           property = Property.objects.get(pk=request.session['property_id'])
           location = Location(property_id=property,nearby_hospital=NearByHospital,nearby_school=NearBySchool,nearby_ATM=NearByATM,nearby_mall=NearByMall,nearby_bank=NearByBank,nearby_grocery_shop=NearByGroceryShop)
           location.save()
           print(request.POST.get('property_id'))
           return redirect('seller_login')
        
        else:
            return render(request,'./NotFound.html')

    else:
        locationform = Location_DetailsForm()
        return render(request,'./location.html',{'form':locationform})

def search(request):
    queryset_list = Property.objects.all()
    images = PropertyImages.objects.all()
    flag=False
    selectedlist=[]
    if 'selected_list' in request.session:
        flag=True
    else:
        flag=False

    if flag==False:
        #city

        if 'city' in request.GET:
            city1 = request.GET['city']
            selectedlist.append(('city',city1))
            print(city1)
            if city1:
                queryset_list = queryset_list.filter(city__iexact=city1)

        #state 

        if 'state' in request.GET:
            state1=request.GET['state']
            selectedlist.append(('state',state1))
            print(state1)

            if state1:
                queryset_list = queryset_list.filter(state__iexact=state1)       

        #housetype

        if 'type_house' in request.GET:
            housetype1=request.GET['type_house']
            selectedlist.append(('housetype',housetype1))
            print(housetype1)

            if housetype1:
                queryset_list = queryset_list.filter(type_house__iexact=housetype1)

        if 'price' in request.GET:
            price1=request.GET['price']
            selectedlist.append(('price',price1))
            price1=int(price1)
            
            if price1:
                queryset_list = queryset_list.filter(price__lte=price1)
        
        if 'floors' in request.GET:
            floors1=request.GET['floors']
            selectedlist.append(('floors',floors1))
            floors1=int(floors1)
            
            if floors1:
                queryset_list = queryset_list.filter(no_of_floors__lte=floors1)
        
        if 'rooms' in request.GET:
            rooms1=request.GET['rooms']
            selectedlist.append(('rooms',rooms1))
            rooms1=int(rooms1)
            
            if rooms1:
                queryset_list = queryset_list.filter(no_of_bedrooms__lte=rooms1)
        
        new_selectedlist=[]
        for tup in selectedlist:
            if tup[1] != '':
                new_selectedlist.append(tup)
        
        request.session['selected_list']=new_selectedlist
        print(request.session['selected_list'])
    else:
        queryset_list=get_querylist(request)
        print(queryset_list)
    
    if len(queryset_list) == 0:
        queryset_list = None
    context={
        'properties':queryset_list,
        'images':images
    }
    
    return render(request,'./searchlist/welcome.html',context)

def get_querylist(request):
    print('method called')
    queryset_list1=Property.objects.all()
    for t in request.session['selected_list']:
        print (t[0])  
        if 'city'== t[0]:
            queryset_list1=queryset_list1.filter(city__iexact=t[1])
        if 'state'== t[0]:
            print('In State')
            queryset_list1=queryset_list1.filter(state__iexact=t[1])
        if 'housetype'== t[0]:
            queryset_list1=queryset_list1.filter(type_house__iexact=t[1])
        if 'price'== t[0]:
            queryset_list1=queryset_list1.filter(price__lte=t[1])
        if 'floors'== t[0]:
            queryset_list1=queryset_list1.filter(no_of_floors__lte=t[1])
        if 'rooms'== t[0]:
            queryset_list1=queryset_list1.filter(no_of_bedrooms__lte=t[1])
    
    return queryset_list1

def property_detail(request, id):
    property_obj = Property.objects.get(pk=id)
    seller_property=property_obj.property_seller
    print(seller_property)
    builder = Builder.objects.get(seller=seller_property)
    print(builder)
    images = PropertyImages.objects.get(property_fk=property_obj)
    specs=property_specs.objects.get(property_id=property_obj)
    nearbys = Location.objects.get(property_id=property_obj)
    context={
        'property_object':property_obj,
        'images':images,
        'specs':specs,
        'nearbys':nearbys,
        'builder':builder
    }
    return render(request,'./Filter/detailedview.html',context)

def compareview(request):
    if request.method=='GET' and request.is_ajax():
        id1= request.GET.get('id1')
        id2= request.GET.get('id2')
        print(id1)
        print(id2)
        image1=list(PropertyImages.objects.filter(property_fk=id1)) 
        image2=list(PropertyImages.objects.filter(property_fk=id2)) 
        queryset = list(Property.objects.filter(pk__in=[id1,id2]))
        return HttpResponse(serializers.serialize('json',queryset+image1+image2),content_type="application/json")

def rendercompareview(request):
    if request.method=='GET' and request.is_ajax():
        obj1=request.GET.get('property1')
        obj2=request.GET.get('property2')

        context={
            'object1':obj1,
            'object2':obj2
        }
        # print(obj1)
        return render(request,'./Compareproperty.html',context)

def send_email(request,emailid,pname):
    seller_email=emailid
    buyermsg=request.POST['buyer_msg']
    print(buyermsg)
    try:
        send_mail('Interested in property',
        'Hi UrbanEstate is glad to inform you that '+request.session['buyer_name']+' is interested in your property '+pname+
        '''
        please contact the buyer through emailId '''+request.session['buyer_email']+'''
        Buyer has coveyed a message to you that is conveyed below 
        '''+buyermsg,
        'pranv315@gmail.com',
        [seller_email],
        fail_silently=False)
        return render(request,'./mailsent.html')
    except:
        return render(request,'./mailnotsent.html')


def take_visit(request,emailid,pname):
    try:
        seller_email=emailid
        date=request.POST['date']
        time=request.POST['time']
        send_mail('Take visit for property',
        'Hi UrbanEstate is glad to inform you that buyer '+request.session['buyer_name']+' wants to take visit at your property named '+pname+
        ' on '+date+''' 
        and at '''+time+''' 
        please contact the buyer through emailId'''+request.session['buyer_email']+'''
        Thank You''',
        'pranv315@gmail.com',
        [seller_email],
        fail_silently=False)
        return render(request,'./schedulevisit.html')
    except:
        return render(request,'./mailnotsent.html')
    

def sellerproperty_detail(request,id):
    print(id)
    property_obj = Property.objects.get(pk=id)
    seller_property=property_obj.property_seller
    print(seller_property)
    builder = Builder.objects.get(seller=seller_property)
    print(builder)
    images = PropertyImages.objects.get(property_fk=property_obj)
    specs=property_specs.objects.get(property_id=property_obj)
    nearbys = Location.objects.get(property_id=property_obj)
    context={
        'property_object':property_obj,
        'images':images,
        'specs':specs,
        'nearbys':nearbys,
        'builder':builder
    }
    return render(request,'./Filter/Seller_View_Details.html',context)

def renderfilterback(request):
    print('rendering again')
    context ={
                'room_choices':room_choices,
                'price_choices':price_choices,
                'floor_choices':floor_choices,
                'state_choices':state_choices,
                'type_house_choices':type_house_choices 
                }
    try:
        del request.session['selected_list']
    except:
        pass
    return render(request,'./Filter/mainpage.html',context)

def back(request):
    querysetlist=request.session['querylist']
    images = PropertyImages.objects.all()
    context={
        'properties':querysetlist,
        'images':images
    }
    return render(request,'./searchlist/welcome.html',context)