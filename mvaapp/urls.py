from django.urls import path
from . import views
urlpatterns=[
   path('',views.formlogin,name='formlogin'),
   path('fun',views.fun,name='fun'),


   path('social',views.social,name='social'),

 path('new',views.new,name='new'),
 path('run',views.run,name='run'),
 path('home',views.home,name='home'),
 path('details',views.details,name='details'),
 path('logout',views.logout,name='logout'),
 path('finedetails',views.finedetails,name='finedetails'),
 path('finalpage',views.finalpage,name='finalpage'),
 path('finealteration',views.finealteration,name='finealteration'),
 path('licenceresult',views.licenceresult,name='licenceresult'),
 path('profile',views.profile,name='profile'),
 path('rto',views.rto,name='rto'),
 path('rtosub',views.rtosub,name='rtosub'),
 path('rtosub',views.rtosub,name='rtosub'),
 path('test',views.test,name='test'),
 path('h',views.h,name='h'),






 
 
 
 
 path('detailsvehicle',views.detailsvehicle,name='detailsvehicle'),
 path('regvehicle',views.regvehicle,name='regvehicle')
 


  
   
   

   
]