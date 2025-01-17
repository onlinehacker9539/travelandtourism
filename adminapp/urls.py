
from django.urls import path
from .views import *

urlpatterns = [
   path('',index.as_view(),name="index"),
   path('addspot',addspot.as_view(),name="addspot"),
   path('addplace',addplace.as_view(),name="addplace"),
   path('festivel',festivel.as_view(),name="festivel"),
  
   path('viewfestivel',viewfestivel.as_view(),name="viewfestivel"),
   path('viewplace',viewplace.as_view(),name="viewplace"),
   path('viewspot',viewspot.as_view(),name="viewspot"),
   path('verifyagent',verifyagent.as_view(),name="verifyagent"),
   path('dashboard1',dashboard1.as_view(),name="dashboard1"),
   path('account_details',account_details.as_view(),name="account_details"),
   path('addlocation',addlocation.as_view(),name="addlocation"),
   path('adminpanel',adminpanel.as_view(),name="adminpanel"),
   path('adminviewalluser',adminviewalluser.as_view(),name="adminviewalluser"),
   path('dashboBookinghistory',dashboBookinghistory.as_view(),name="Bookinghistory"),
   path('dayplanneradd',dayplanneradd.as_view(),name="dayplanneradd"),
   path('dayplanneredit',dayplanneredit.as_view(),name="dayplanneredit"),
   path('dayplannermanage',dayplannermanage.as_view(),name="dayplannermanage"),
   path('getlocation',getlocation.as_view(),name="getlocation"),
   path('hoteladd',hoteladd.as_view(),name="hoteladd"),
   path('hoteledit',hoteledit.as_view(),name="hoteledit"),
   path('hotelmanage',hotelmanage.as_view(),name="hotelmanage"),
   path('index',index.as_view(),name="index"),
   path('login',login.as_view(),name="login"),
   path('packagedetailsadd',packagedetailsadd.as_view(),name="packagedetailsadd"),
   path('packagedetailsedit',packagedetailsedit.as_view(),name="packagedetailsedit"),
   path('packagedetailsmanage',packagedetailsmanage.as_view(),name="packagedetailsmanage"),
   path('packageplaceadd',packageplaceadd.as_view(),name="packageplaceadd"),
   path('packageplaceedit',packageplaceedit.as_view(),name="packageplaceedit"),
   path('packageplacemanage',packageplacemanage.as_view(),name="packageplacemanage"),
   path('registraction',registraction.as_view(),name="registraction"),
   path('savelocation',savelocation.as_view(),name="savelocation"),
   path('userbookingpackage',userbookingpackage.as_view(),name="userbookingpackage"),
   path('userviewdayplanner',userviewdayplanner.as_view(),name="userviewdayplanner"),
   path('userviewpackage',userviewpackage.as_view(),name="userviewpackage"),
   path('userviewpackageplace',userviewpackageplace.as_view(),name="userviewpackageplace"),
   path('festivel',festivel.as_view(),name="festivel"),
]



