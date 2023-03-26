from django.urls import path
from . import views

#http://127.0.0.1:8080/FirstApp/
urlpatterns = [
    path('',views.listPatients,name='list_patients')
]
