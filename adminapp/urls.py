
from django.urls import path
from .views import *

urlpatterns = [
   path('',index.as_view(),name="index"),
   path('sample',adminapp.as_view(),name="sample"),
   path('addspot',addspot.as_view(),name="addspot"),
   path('addplace',addplace.as_view(),name="addplace"),
   path('dashboard',dashboard.as_view(),name="dashboard"),
   path('festivel',festivel.as_view(),name="festivel"),
  
   path('viewfestivel',viewfestivel.as_view(),name="viewfestivel"),
   path('viewplace',viewplace.as_view(),name="viewplace"),
   path('viewspot',viewspot.as_view(),name="viewspot"),
   path('verifyagent',verifyagent.as_view(),name="verifyagent")
]



