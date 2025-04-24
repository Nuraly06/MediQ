from django import forms
from .models import Appointment,Doctor,Service

class AppointmentForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your name','style':'margin-top:2%;'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter your Email','style':'margin-top:2%;'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your phone','style':'margin-top:2%;'}))
    doctor = forms.ModelChoiceField(
        queryset = Doctor.objects.all(),
        empty_label="Select a doctor",
        widget=forms.Select(attrs={'class':'form-control','style':'margin-top:2%;'})
    )
    service = forms.ModelChoiceField(
        queryset= Service.objects.all(),
        empty_label="Select a service",
        widget=forms.Select(attrs={'class':'form-control','style':'margin-top:2%;'})

    )
    date = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','type':'date','style':'margin-top:2%;'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'class':'form-control','type':'time','style':'margin-top:2%;'}))



 
  

    class Meta:
        model = Appointment
        fields=['name','email','phone','doctor','service','date','time']



class Search_Doctor(forms.ModelForm):
    doctor = forms.ModelChoiceField(
        queryset = Doctor.objects.all(),
        empty_label="Select a doctor",
        widget=forms.Select(attrs={'class':'form-control','style':'margin-top:2%;'})
    )
   

    class Meta:
        model = Appointment
        fields=['doctor']