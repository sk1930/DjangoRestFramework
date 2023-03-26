from django.urls import path
from . import views
# we can also write this as from views import index 


#     path('',views.index,name='index') here 1st param is route as it is empty it is accessible at /firstapp
# the view is views.index and the name is just needed for referenfces

urlpatterns=[
    path('',views.index,name='index')
    
]
