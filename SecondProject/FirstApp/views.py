from django.shortcuts import render

# Create your views here.
# http://127.0.0.1:8080/FirstApp/
def example_view(request):
    #FirstApp/templates/FirstAppp/example.html
    return render(request,"FirstApp/example.html")

# http://127.0.0.1:8080/FirstApp/variable/
def variable_view(request):
    my_Var={'first_name':"saikrishna",'last_name':'padamatintI',
    'some_list':[1,2,4],'some_dict':{'inside_key':'inside_value'},
    "user_logged_in":True
    }
    #FirstApp/templates/FirstAppp/example.html
    return render(request,"FirstApp/variable.html",context=my_Var)