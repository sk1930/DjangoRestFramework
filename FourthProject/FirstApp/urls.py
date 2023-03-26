from django.urls import path
from . import views

#to be able to use urlnames along with app name using tags in base.html
app_name='FirstApp' 

#domain.com/cars/list
urlpatterns = [
    path('list/',views.list,name="list"),
    path('add/',views.add,name="add"),
    path('delete/',views.delete,name="delete")

]
