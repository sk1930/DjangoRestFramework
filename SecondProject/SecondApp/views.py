from django.shortcuts import render

# Create your views here.
# http://127.0.0.1:8080/SecondApp/
def example_view(request):
    return render(request,"SecondApp/example.html")

# http://127.0.0.1:8080/SecondApp/variable/
def variable_view(request):
    return render(request,"SecondApp/variable.html")

def inheritance_view(request):
    return render(request,"SecondApp/inheritance.html")

# http://127.0.0.1:8080/SecondApp/image_static/
def image_static_view(request):
    return render(request,"SecondApp/image.html")
