from django.db import models

# Create your models here.





class drivinglicence(models.Model):
    Licenceid=models.CharField(max_length=10)
    Name=models.CharField(max_length=10)
    Address=models.CharField(max_length=10)
    Bloodgroup=models.CharField(max_length=10)
    Dob=models.CharField(max_length=10)
    validfrom=models.CharField(max_length=10)
    validto =models.CharField(max_length=10)
    vehicleclass =models.CharField(max_length=10)
    img=models.ImageField(upload_to="images")


class fine(models.Model):
    Licenceid=models.CharField(max_length=10)
    fines=models.CharField(max_length=10)
    date=models.CharField(max_length=10)
    location=models.CharField(max_length=10)
    status=models.CharField(max_length=10)

class vehiclefine(models.Model):
    vehicleid=models.CharField(max_length=10)
    fines1=models.CharField(max_length=10)
    fines2=models.CharField(max_length=10) 
    fines3=models.CharField(max_length=10)

class vehicledetails(models.Model):
    NAME=models.CharField(max_length=10)
    ADDRESS=models.CharField(max_length=10)
    REGISTRATIONNO=models.CharField(max_length=10)
    CHASSISNO=models.CharField(max_length=10) 
    ENGINENO=models.CharField(max_length=10)
    MAKERNAME=models.CharField(max_length=10)
    MODELNAME=models.CharField(max_length=10)
    MODELDESC=models.CharField(max_length=10) 
    REGISTRATIONDATE=models.CharField(max_length=10)
    RCSTATUS=models.CharField(max_length=10)
    TAXVALIDUPTO=models.CharField(max_length=10)
    PUCCNO=models.CharField(max_length=10)
    PUCCVALIDUPTO=models.CharField(max_length=10) 
    FUELTYPE=models.CharField(max_length=10)
    COLOR=models.CharField(max_length=10)
    SEATCAPACITY=models.CharField(max_length=10)
    INSURANCEPOLICYNO=models.CharField(max_length=10) 
    INSURANCEVALIDUPTO=models.CharField(max_length=10)
    FITNESSVALIDUPTO=models.CharField(max_length=10) 
    REGISTERINGAUTHORITY=models.CharField(max_length=10)
    img=models.ImageField(upload_to="images")
class regfine(models.Model):
    REGISTRATIONNO=models.CharField(max_length=10)
    fines=models.CharField(max_length=10)
    date=models.CharField(max_length=10)
    location=models.CharField(max_length=10)
    status=models.CharField(max_length=10)

class alterationfine(models.Model):
    REGISTRATIONNO=models.CharField(max_length=10)
    fines=models.CharField(max_length=10)
    date=models.CharField(max_length=10)
    location=models.CharField(max_length=10)
    status=models.CharField(max_length=10)
class status(models.Model):
    image=models.ImageField(upload_to="pictures")
    name=models.CharField(max_length=10)
    spec=models.CharField(max_length=10)
    rate=models.CharField(max_length=10)      
               
           

               
           
  

        

     
   
    
        