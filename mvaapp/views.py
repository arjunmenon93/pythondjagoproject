



from asyncio.windows_events import NULL
from email import message
from multiprocessing import context
from pickle import NONE
from unittest import loader
from urllib import response
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import  authenticate ,login
from flask import request





from .models import drivinglicence
from .models import fine
from .models import vehiclefine
from .models import vehicledetails
from .models import regfine
from .models import alterationfine



# Create your views here.
def fun(request):
    if request.method=="POST":

    
        
        user_name = request.POST['name']
        idnumber = request.POST['idnumber']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['eemail']
        phonenumber=request.POST['phonenumber']
        if password1==password2:
         if User.objects.filter(idnumber=idnumber).exists():
                messages.info(request,"id taken")
                return render(request,"reg.html")
         elif User.objects.filter(email=email).exists():
                messages.info(request,"email is already taken")
                ##return redirect('register')
         else:
          u=User.objects.create_user(username=user_name,idnumber=idnumber,password=password1,password1=password2,email=email,phonenumber=phonenumber)
          u.save();
          print("user created")
          messages.info(request, "succesfuly")
          return render(request,'login.html')
        #messages.info(request,"succesfuly")
    # messages.info(request,"username taken")
        else:
            messages.info(request,"password does not match")
            return render(request,'reg.html')
    else:
        return render(request,"reg.html")



def social(request):
    if request.method=="POST":

        name=request.POST['name']
        eemail = request.POST['eemail']
        phonenumber = request.POST['phonenumber']
        idnumber=request.POST['idnumber']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1==password2:
         if person.objects.filter(Idnumber=idnumber).exists():
                messages.info(request,"Please check Idnumber")
                return render(request,"register.html")
         elif person.objects.filter(Email=eemail).exists():
                messages.info(request,"Email is already taken")
                return render(request,"register.html")
         else:
          u=person.objects.create(Username=name,Email=eemail,Phonenumber=phonenumber,Idnumber=idnumber,password1=password1)
          u.save();
          print("user created")
          messages.info(request, "Successfully Registered")
          return render(request,'login.html')
        #messages.info(request,"succesfuly")
         # messages.info(request,"username taken")
        else:
            messages.info(request,"Password does not match")
            return render(request,'register.html')
    else:
        return render(request, "register.html")
def formlogin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        id=request.POST['ID']
        
        u=auth.authenticate(Username=username,password1=password,id=id)
        
        if u is None:
            auth.login(request,u)

         
         
            
            return render(request,'rough.html')
            
        else:

           return redirect(formlogin)

            
            
    else:
        return render(request,"login.html")

        
def new(request):
    if request.method=="POST":

        

        user_name = request.POST['user_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        id=request.POST['id']
        if password1==password2:
         if User.objects.filter(id=id).exists():
                messages.info(request,"Id is already taken")
                return render(request,"r.html")
         elif User.objects.filter(email=email).exists():
                messages.info(request,"Email is already taken")
                return render(request,"r.html")
                
         else:
          user=User.objects.create_user(username=user_name,password=password1,id=id,email=email,last_name=password2)
          user.save();
          print("user created")
          messages.info(request, "Successfully Registered")
          return render(request,'login.html')
        #messages.info(request,"succesfuly")
    # messages.info(request,"username taken")
        else:
            messages.info(request,"Password does not match")
            return render(request,'r.html')
            
    else:
        return render(request,"r.html")

def run(request):
    

    
        

    
        
      if request.method=="POST":
       
            
        user_name=request.POST['user_name']
        password=request.POST['password1']
        
        
        
        user = auth.authenticate(username=user_name,password=password)
        if user is not None:
            auth.login(request,user)

            return redirect(home)
          
            #return redirect('/')
        else:
            messages.info(request,"Invalid Username or Password")
            return  redirect(run)
      else:
        return render(request,"login.html")
    



def home(request):
    if request.user.is_authenticated:
      return render(request,'rough.html')
    else:
        return render(request,'login.html')


    
            
       
def details(request):
 if request.user.is_authenticated: 
    if request.method=="POST":
           Licenceid=request.POST['licence']
           if drivinglicence.objects.filter(Licenceid=Licenceid).exists():
            m = drivinglicence.objects.filter(Licenceid=Licenceid)
            j = fine.objects.filter(Licenceid=Licenceid)
            return  render(request,"result.html",{"messages":m,"mk":j})
           else:
            messages.info(request,"Invalid Licence Number")
            return render(request,"dtbackup.html")
    else:   

     return  render(request,"dtbackup.html")
 else:
     return  render(request,"login.html")
def detailsvehicle(request):
   if request.user.is_authenticated: 
    if request.method=="POST":
           reg=request.POST['registration']
           if vehicledetails.objects.filter(REGISTRATIONNO=reg).exists():
            z = vehicledetails.objects.filter(REGISTRATIONNO=reg)
            o=regfine.objects.filter(REGISTRATIONNO=reg)
            k=alterationfine.objects.filter(REGISTRATIONNO=reg)
            return  render(request,"test.html",{"me":z,"ie":o,"i":k})
           else:
            messages.info(request,"Invalid Registration Number ")
            return render(request,"dtbackup.html") 
    else:
         return render(request,"dtbackup.html") 
   else:
     return  render(request,"login.html")         


                     

         

  
         


       
def logout(request):
    auth.logout(request)
    
    return redirect(run)

from datetime import datetime
now = datetime.now()
date_time=now.strftime("%m/%d/%y,%H:%M:%S")
def finedetails(request): 
    if request.method=="POST":
        Licenceid =request.POST['licence']
        anu=request.POST.getlist('vehicle')
        loc=request.POST['location']
        manu=request.POST['unpaid']
        if drivinglicence.objects.filter(Licenceid=Licenceid).exists():
         l=fine.objects.create(Licenceid=Licenceid,fines=anu,date=date_time,location=loc,status=manu)
         l.save();
        else:
            messages.info(request,"Invalid licence number")

    return render(request,'check1.html') 
    
from datetime import datetime
now = datetime.now()
date_time=now.strftime("%m/%d/%y,%H:%M:%S")
def regvehicle(request):
 if request.user.is_authenticated:  
    if request.method=="POST":
     reg =request.POST['registration']
     kl=request.POST.getlist('bike')
     lo=request.POST['location']
     ma=request.POST['unpaid']

     if vehicledetails.objects.filter(REGISTRATIONNO=reg).exists():
          o=regfine.objects.create(REGISTRATIONNO=reg,fines=kl,date=date_time,location=lo,status=ma)
          o.save();
     else:
            messages.info(request,"Invalid registration number")
            return render(request,'check1.html')
 else:
     
    return  render(request,"login.html") 
 return render(request,'check1.html')
def finalpage(request):
    return  render(request,'final.html')

from datetime import datetime
now = datetime.now()
date_time=now.strftime("%m/%d/%y,%H:%M:%S")
def finealteration(request): 
  if request.method=="POST":
    reg =request.POST['registration']
    kl=request.POST.getlist('a')
    lo=request.POST['location']
    ma=request.POST['unpaid']
    if vehicledetails.objects.filter(REGISTRATIONNO=reg).exists():
          k=alterationfine.objects.create(REGISTRATIONNO=reg,fines=kl,date=date_time,location=lo,status=ma)
          k.save();
    else:
         messages.info(request,"Invalid registration number")
         return render(request,'final.html')
   
  return  render(request,'final.html')

def licenceresult(request):
    return render(request,"result.html")  

def profile(request):
    return render(request,'profile.html')

def rto(request):
    return render(request,'rto.html')

def rtosub(request):
    return render(request,'rtosub.html')


from .models import alterationfine

def test (request):
    o = alterationfine.objects.all()
    context = {
    'l': o
  }
    return render(request,"hari.html",context)
   
def h (request):
    return render(request,"hari.html")
        
    
    



  

 






    

        
    
    
    
        
         

    

        

        
    

    
        


    
           
        
            
        

     
         
       

          

            
        
    
           

        
        
              




              
