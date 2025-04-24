from django.urls import path
from . import views

urlpatterns=[
    
    path('',views.Home,name='Home'),
    path('appointment/',views.AppointmentView,name='appointment'),
    path('about/',views.about,name='about'),
   
]