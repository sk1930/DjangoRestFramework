from django.shortcuts import render


# Create your views here.
#http://127.0.0.1:8000/thirdapp/
def simple_view(request):
    return render(request,'ThirdApp/example.html') # there is some html file 
    # render takes 3 args mainly request: HttpRequest, template_name: str | Sequence[str], context:\
    # context is whats that is passed back to the template file