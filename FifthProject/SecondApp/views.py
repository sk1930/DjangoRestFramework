from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import ReviewForm
# we import forms.py here
# Create your views here.
def rental_review(request):
    # POST request ---> form contents -- > thank you 

    if request.method =='POST':
        form = ReviewForm(request.POST)
        #form = ReviewForm(request.POST) binds the data to the form class so Django can do fun stuff like validate inputs with is_valid().

        if form.is_valid(): # this is checking for the max lenght and email for email field is passed or not
            print(form.cleaned_data)            
            form.save()

            '''{'first_name': 'sak', 'last_name': 'anc', 'email': 'saikrishna1930@gmail.com', 'review': 'sddff'}'''
            return redirect(reverse('SecondApp:thank_you'))
    #ELSE RENDER THE FORM
    else:
        form = ReviewForm()
    # its better to keep the return out of all if and else so that something will be returned for sure
    return render(request,'SecondApp/rental_review.html',context={'form':form})

def thank_you(request):
    return render(request,'SecondApp/thank_you.html')
