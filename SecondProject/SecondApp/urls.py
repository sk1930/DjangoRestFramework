
from django.contrib import admin
from django.urls import path
from . import views

# register the app namespace
# URL names
app_name = 'SecondApp'
urlpatterns = [
    path('',views.example_view,name='example'),
    path('variable/',views.variable_view,name='variable'),
    path('inheritance/',views.inheritance_view,name='inheritance'),
    path('image_static/',views.image_static_view,name='image_static'),

    


]

