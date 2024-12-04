
from django.urls import path
from .views import *

urlpatterns = [
   path('sample',adminapp.as_view(),name="sample"),
   path('addspot',addspot.as_view(),name="addspot"),
   path('addplace',addplace.as_view(),name="addplace"),
   path('dashboard',dashboard.as_view(),name="dashboard"),
   path('festivel',festivel.as_view(),name="festivel"),
   path('index',index.as_view(),name="index"),
   path('viewfestivel',viewfestivel.as_view(),name="viewfestivel"),
   path('viewplace',viewplace.as_view(),name="viewplace"),
   path('viewspot',viewspot.as_view(),name="viewspot")
]



