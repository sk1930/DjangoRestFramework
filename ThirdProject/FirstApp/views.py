from django.shortcuts import render
from .  import models # to import Patient
# Create your views here.

#http://127.0.0.1:8080/FirstApp/
def listPatients(request):
    all_patients = models.Patient.objects.all()
    context = {'patients':all_patients}
    return render(request,'FirstApp/list.html',context=context)