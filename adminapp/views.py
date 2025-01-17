from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from adminapp.models import LoginTable
# Create your views here.

class index(View):
    def get(self,request):
        return render(request,"login.html")  
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        login_obj = LoginTable.objects.get(username=username, password=password)
        if login_obj.usertype == "admin":
            return HttpResponse('''<script>alert("welcome to a");window.location="/dashboard1"</script>''')
        elif login_obj.usertype == "travelagent":
            return HttpResponse('''<script>alert("welcome to a");window.location=""</script>''')
        elif login_obj.usertype == "restaurant":
            return HttpResponse('''<script>alert("welcome to a");window.location=""</script>''')
        

class adminapp(View):
    def get(self,request):
        return render(request,"adminapp.html")

class addspot(View):
    def get(self,request):
        return render(request,"add spot.html")

class addplace(View):
    def get(self,request):
        return render(request,"add place.html")

class dashboard1(View):
    def get(self,request):
        return render(request,"dashboard1.html")     

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
    
class account_details(View):
    def get(self,request):
        return render(request,"account_details.html")

class addlocation(View):
    def get(self,request):
        return render(request,"addlocation.html")  
    
class adminpanel(View):
    def get(self,request):
        return render(request,"adminpanel.html")  
    
class adminviewalluser(View):
    def get(self,request):
        return render(request,"adminviewalluser.html")  
    
class dashboaradminviewbooking(View):
    def get(self,request):
        return render(request,"dashboaradminviewbooking.html")  
    
class dashboBookinghistory(View):
    def get(self,request):
        return render(request,"dashboBookinghistory.html")  
    
class dayplanneradd(View):
    def get(self,request):
        return render(request,"dayplanneradd.html")  
    
class dayplanneredit(View):
    def get(self,request):
        return render(request,"dayplanneredit.html")  
    
class dayplannermanage(View):
    def get(self,request):
        return render(request,"dayplannermanage.html")  
    
class getlocation(View):
    def get(self,request):
        return render(request,"getlocation.html")  
    
class hoteladd(View):
    def get(self,request):
        return render(request,"hoteladd.html")  
    
class hoteledit(View):
    def get(self,request):
        return render(request,"hoteledit.html")  
    
class hotelmanage(View):
     def get(self,request):
         return render(request,"hotelmanage.html")  
    
class login(View):
     def get(self,request):
         return render(request,"login.html")  
class packagedetailsadd(View):
     def get(self,request):
         return render(request,"packagedetailsadd.html")  
    
class packagedetailsedit(View):
     def get(self,request):
         return render(request,"packagedetailsedit.html")  
    
class packagedetailsmanage(View):
     def get(self,request):
         return render(request,"packagedetailsmanage.html")  
    
class packageplaceadd(View):
     def get(self,request):
         return render(request,"packageplaceadd.html")  
     
class packageplaceedit(View):
     def get(self,request):
         return render(request,"packageplaceedit.html")  
    
    
class packageplacemanage(View):
     def get(self,request):
         return render(request,"packageplacemanage.html")  
    
class registraction(View):
     def get(self,request):
         return render(request,"registraction.html")  
    
class savelocation(View):
     def get(self,request):
         return render(request,"savelocation.html")  
    
class userbookingpackage(View):
     def get(self,request):
         return render(request,"userbookingpackage.html")  
    
class userviewdayplanner(View):
     def get(self,request):
         return render(request,"userviewdayplanner.html")  
    
class userviewpackage(View):
     def get(self,request):
         return render(request,"userviewpackage.html")  
    
class userviewpackageplace(View):
     def get(self,request):
         return render(request,"userviewpackageplace.html")  
    
class festivel(View):
     def get(self,request):
         return render(request,"festivel.html")  
    
