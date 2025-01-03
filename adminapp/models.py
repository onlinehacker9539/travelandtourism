from django.db import models

# Create your models here.
class LoginTable(models.Model):
    username=models.CharField(max_length=200,null=True,blank=True)
    password=models.CharField(max_length=200,null=True,blank=True)
    usertype=models.CharField(max_length=200,null=True,blank=True)

class Travelagenttable(models.Model):
    loginid=models.ForeignKey(LoginTable, on_delete=models.CASCADE, null=True)
    name=models.CharField(max_length=200,null=True,blank=True)
    address=models.CharField(max_length=200,null=True,blank=True)
    mailid=models.CharField(max_length=200,null=True,blank=True)
    phonenumber=models.BigIntegerField(null=True,blank=True)
    idproof=models.CharField(max_length=200,null=True,blank=True)
    licencenumber=models.BigIntegerField(null=True,blank=True)

class places(models.Model):
    place=models.CharField(max_length=200,null=True,blank=True)
    details=models.CharField(max_length=200,null=True,blank=True)

class spots(models.Model):
    spotname=models.CharField(max_length=200,null=True,blank=True)
    placename=models.CharField(max_length=200,null=True,blank=True)
    description=models.CharField(max_length=200,null=True,blank=True)
    image=models.FileField(upload_to="spots/",null=True,blank=True)
    

class festivels(models.Model):
    festivelname=models.CharField(max_length=200,null=True,blank=True)
    place=models.CharField(max_length=200,null=True,blank=True)
    date=models.DateField(null=True,blank=True)
    description=models.CharField(max_length=200,null=True,blank=True)
    location=models.CharField(max_length=200,null=True,blank=True)

class Package_detail(models.Model):
    package_name=models.CharField(max_length=250)
    place= models.ForeignKey(places,on_delete=models.CASCADE)
    package_type=models.CharField(max_length=250)
    description=models.TextField()
    image = models.FileField(upload_to='images')
    total_days=models.CharField(max_length=250)
    total_amount=models.DecimalField(max_digits=10,decimal_places=2)
    inclusion=models.CharField(max_length=250)
    def _str_(self):
        return str(self.package_name)
    
class restaurant(models.Model):
    restaurantname=models.CharField(max_length=100,null=True,blank=True)
    place=models.CharField(max_length=200,null=True,blank=True)
    phone=models.BigIntegerField(null=True,blank=True)
    email=models.CharField(max_length=200,null=True,blank=True)
    location=models.CharField(max_length=200,null=True,blank=True)

class usertable(models.Model):
    name=models.CharField(max_length=200,null=True,blank=True)
    age=models.IntegerField(null=True,blank=True)
    gender=models.CharField(max_length=100,null=True,blank=True)
    address=models.CharField(max_length=200,null=True,blank=True)
    phone=models.BigIntegerField(null=True,blank=True)
    email=models.CharField(max_length=100,null=True,blank=True)