from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.

class index(View):
    def get(self,request):
        
        return render(request,"index.html")  
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        login_obj = LoginTable.objects.get(Username=username, Password=password)
        if login_obj.Type == "admin":

            return HttpResponse(<script>alert("welcome to a");window.location="" )








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

class viewfestivel(View):
    def get(self,request):
        return render(request,"view festivel.html")  
class viewplace(View):
    def get(self,request):
        return render(request,"view place.html")  
class viewspot(View):
    def get(self,request):
        return render(request,"viewspot.html")  
    
class verifyagent(View):
    def get(self,request):
        return render(request,"verifyagent.html")  
