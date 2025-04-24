from django.db import models

# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length=200)
    email=models.EmailField()
    phone = models.CharField(max_length=30) 
    specialization=models.CharField(max_length=200)
    experience=models.IntegerField()
    available_days=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name
    

class Service(models.Model):
     name = models.CharField(max_length=200) 
     description = models.TextField(blank=True, null=True) 
     price = models.DecimalField(max_digits=10, decimal_places=2)   
     duration = models.DurationField(null=True, blank=True)  
     created_at = models.DateTimeField(auto_now_add=True)    

     def __str__(self):
         return f"{self.name} - {self.price} .eg"




class Patient(models.Model):
     name = models.CharField(max_length=200)
     email= models.EmailField()
     phone= models.CharField(max_length=30)
     created_at= models.DateTimeField(auto_now_add=True)

     def __str__(self):
         return self.name+"_"+self.phone

class Appointment(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    service = models.ForeignKey(Service,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email= models.EmailField()
    phone= models.CharField(max_length=30)
    date = models.DateField()
    time = models.TimeField()
    def __str__(self):
        return f"{self.patient.name} - {self.doctor.name} - {self.service.name} ({self.date} {self.time})"
    


