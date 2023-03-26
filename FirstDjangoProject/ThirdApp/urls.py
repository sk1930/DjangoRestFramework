from django.urls import path
from . import views



# path('',views.simple_view) connects to domain.com/ThirdApp

urlpatterns=[
    path('',views.simple_view),

]    