
from .models import Builder,Seller
from django.contrib.auth import get_user_model
from django.template.context_processors import csrf
from django.shortcuts import redirect, render
from .forms import BuilderForm,SellerSignUpForm

def save_builder(request):
    if request.method =='POST':
        form =  BuilderForm(request.POST,request.FILES)
        if form.is_valid():
            landmark_projects = form.cleaned_data.get('landmark_projects')
            current_projects = form.cleaned_data.get('current_projects')
            Rera_Certificate = form.cleaned_data.get('Rera_Certificate')
            lawyer = form.cleaned_data.get('lawyer')
            architect = form.cleaned_data.get('architect')
            chartered_acc = form.cleaned_data.get('chartered_acc')
            site_incharge = form.cleaned_data.get('site_incharge')
            sales_team_rep = form.cleaned_data.get('sales_team_rep')
            project_duration = form.cleaned_data.get('project_duration')
            bank_tie_ups = form.cleaned_data.get('bank_tie_ups')
            Youtube_channel=form.cleaned_data.get('Youtube_channel')
            facebook_handle=form.cleaned_data.get('facebook_handle')
            Twitter_handle=form.cleaned_data.get('Twitter_handle')
            embed_link=form.cleaned_data.get('Embed_link')
            seller = Seller.objects.get(pk=request.session['seller_pk'])
            builder=Builder(seller=seller,landmark_projects=landmark_projects,current_projects=current_projects,Rera_Certificate=Rera_Certificate,lawyer=lawyer,architect=architect,chartered_acc=chartered_acc,site_incharge=site_incharge,sales_team_rep=sales_team_rep,project_duration=project_duration,bank_tie_ups=bank_tie_ups,Youtube_channel=Youtube_channel,facebook_handle=facebook_handle,Twitter_handle=Twitter_handle,Embed_link=embed_link)
            builder.save()
            
            #return render(request,'./propertycreate.html',{'builder':builder})
            return redirect('property_create')
        else:
            return render(request,'./registration/details.html',{'form':form})
    else:
        fm = BuilderForm()
        return render(request,'./registration/details.html',{'form':fm})            
            
            
