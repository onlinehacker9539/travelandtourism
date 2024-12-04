from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.
class adminapp(View):
    def get(self,request):
        return render(request,"adminapp.html")

class addspot(View):
    def get(self,request):
        return render(request,"add spot.html")

class addplace(View):
    def get(self,request):
        return render(request,"add place.html")

class dashboard(View):
    def get(self,request):
        return render(request,"dashbord1.html")     

class festivel(View):
    def get(self,request):
        return render(request,"festivel.html")  
class index(View):
    def get(self,request):
        return render(request,"index.html")  
class viewfestivel(View):
    def get(self,request):
        return render(request,"view festivel.html")  
class viewplace(View):
    def get(self,request):
        return render(request,"view place.html")  
class viewspot(View):
    def get(self,request):
        return render(request,"viewspot.html")  
