from django.db import models

# Create your models here.
class LoginTable(models.Model):
    username=models.CharField(max_length=200,null=True,blank=True)
    password=models.CharField(max_length=200,null=True,blank=True)
    usertype=models.CharField(max_length=200,null=True,blank=True)
class Travelagenttable(models.Model):
    loginid=models.Foreignkey(Logintable, on_delete=model.CASCADE)
    name=models.CharField(max_length=200,null=True,blank=True)
    address=models.CharField(max_length=200,null=True,blank=True)
    mailid=models.email(max_length=200,null=True,blank=True)
    phonenumber=models.number(max_length=200,null=True,blank=True)
    idproof=models.CharField(max_length=200,null=True,blank=True)
    licencenumber=models.number(max_length=200,null=True,blank=True)
class places(models.Model):
    place=models.CharField(max_length=200,null=True,blank=True)

class spots(models.Model):
    spotname=models.CharField(max_length=200,null=True,blank=True)
    placename=models.CharField(max_length=200,null=True,blank=True)
    description=models.CharField(max_length=200,null=True,blank=True)
    image=models.FileField(null=True,blank=True)
    vr=models.FileField()

class festivels(models.Model):
    festivelname=models.CharField(max_length=200,null=True,blank=True)
    place=models.CharField(max_length=200,null=True,blank=True)
    date=models.DateFeild(null=True,blank=True)
    description=models.CharField(max_length=200,null=True,blank=True)
    location=models.CharField(max_length=200,null=True,blank=True)
    
class restaurant(models.Model):
    pass

