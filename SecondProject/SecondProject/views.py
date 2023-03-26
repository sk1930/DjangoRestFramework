from django.shortcuts import render

# frunction name can be anything but lets macth with the name in documentation 
# along with request it has exception as the 2nd argument
def my_custom_page_not_found_view(request,exception):
    return render(request,"error_view.html",status=404)
