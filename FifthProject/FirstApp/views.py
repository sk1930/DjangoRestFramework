from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import ReviewForm
# we import forms.py here
# Create your views here.
def rental_review(request):
    # POST request ---> form contents -- > thank you 

    if request.method =='POST':
        form = ReviewForm(request.POST)
        if form.is_valid(): # this is checking for the max lenght and email for email field is passed or not
            print(form.cleaned_data)
            '''{'first_name': 'sak', 'last_name': 'anc', 'email': 'saikrishna1930@gmail.com', 'review': 'sddff'}'''
            return redirect(reverse('FirstApp:thank_you'))
    #ELSE RENDER THE FORM
    else:
        form = ReviewForm()
        # here we are storing the ReviewForm in form and passing it in context below
    # its better to keep the return out of all if and else so that something will be returned for sure
    return render(request,'FirstApp/rental_review.html',context={'form':form})

def thank_you(request):
    return render(request,'FirstApp/thank_you.html')
