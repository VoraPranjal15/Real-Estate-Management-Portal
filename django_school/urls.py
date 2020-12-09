from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 
from django.urls import include, path
from users.views import buyers, seller, signup
from django.contrib import admin
from users import views1
from . import settings

urlpatterns = [
    path('admin/',admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', signup.SignUpView.as_view(), name='signup'),
    path('signup/buyer/', buyers.BuyerSignUpView.as_view(), name='buyer_signup'),
    path('signup/seller/', seller.SellerSignUpView.as_view(), name='seller_signup'),
    path('s_logout/',seller.logout_request,name='seller_logout'),
    path('signup/seller/registration/login/',seller.login_request,name='seller_login'),
    path('b_login/',buyers.login_request,name='buyer_login'),
    path('b_logout/',buyers.logout_request,name='buyer_logout'),
    path('property/',include('property.urls')),
    #path('form/',seller.BuilderformView.as_view(),name='builderform'),
    path('signup/seller/registration/details/',views1.save_builder,name='builderform'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

