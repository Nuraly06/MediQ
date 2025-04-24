from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib import messages


# Create your views here.
from .forms import AppointmentForm
from .models import Patient

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AppointmentForm,Search_Doctor
from .models import Patient, Appointment ,Doctor
import hashlib

def AppointmentView(request):
    form = AppointmentForm()
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)

            Name = form.cleaned_data['name']
            Email = form.cleaned_data['email']
            Phone = form.cleaned_data['phone']

            patient , created = Patient.objects.get_or_create(
                email = Email,
                defaults={'name':Name,'phone':Phone}
            )
            appointment.patient = patient
            appointment.save()
            return redirect('Home')

    return render(request, 'appointment.html', {'form': form})



def Home(request):
    form = Search_Doctor()
    days = ""     

    if request.method == 'POST':
        form = Search_Doctor(request.POST)
        if form.is_valid():
            Name = form.cleaned_data['doctor']
            doctor = Doctor.objects.filter(name=Name).first()
            if doctor:
                days = doctor.available_days     
            return JsonResponse({"days": days})

    return render(request, 'Home.html', {'form': form}) 



def about(request):
    
    
    

    return render(request, 'about.html', {})

    




    



    
