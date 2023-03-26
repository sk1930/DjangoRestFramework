from django.shortcuts import render,redirect
from django.urls import reverse
from . import models
# Create your views here.
def add(request):
    if request.POST:
        brand=request.POST['brand']
        year=int(request.POST['year'])
        models.Car.objects.create(brand=brand,year=year)
        return redirect(reverse('FirstApp:list'))
    else:
        # when the add page is opened for the first time it
        # comes to this else
        # and when submit is clicked we are not going anywhere as
        # form action is empty 
        # so it hits the same url again but with post
        return render(request,'FirstApp/add.html')
    
def list(request):
    all_Cars = models.Car.objects.all()
    context = {'all_cars':all_Cars}
    return render(request,'FirstApp/list.html',context=context)
    
def delete(request):

    if request.POST:
        pk=request.POST['pk']
        try:
            car1=models.Car.objects.get(pk=pk).delete()
            return redirect(reverse('FirstApp:list'))
        except:
            print(f"pk {pk } not found")
            return redirect(reverse('FirstApp:delete'))
    else:
        # when the add page is opened for the first time it
        # comes to this else
        # and when submit is clicked we are not going anywhere as
        # form action is empty 
        # so it hits the same url again but with post 
        return render(request,'FirstApp/delete.html')