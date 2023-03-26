from django.urls import path
from . import views

# app_name is needed to use the url names later on in redirect nad reverse
app_name="SecondApp"
urlpatterns = [
    path('rental_review/',views.rental_review,name='rental_review'),
    path('thank_you/',views.thank_you,name='thank_you')

]
