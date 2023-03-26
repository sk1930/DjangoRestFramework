from django.shortcuts import render
from django.http import HttpResponse
from .models import Book,Author,BookInstance,Genre,Language 
from django.views.generic import CreateView,DetailView,ListView 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.forms import UserCreationForm 
from django.urls import reverse_lazy 

'''# Create your views here.
def index(request):
    return HttpResponse("Hello")
    # if u notice this it doesnt have any html page in the templates we are just returning the HttpResponse
'''
def index(request):

    num_books= Book.objects.all().count() 
    num_instances = BookInstance.objects.all().count() 

    num_instances_avail = BookInstance.objects.filter(status__exact='a').count()
    # status__exact --status is the field __exact is the operator    

    context = {
        'num_books':num_books,
        'num_instances':num_instances,
        'num_instances_avail':num_instances_avail
    }

    return render(request,'FirstApp/index.html',context=context)



class BookCreate(LoginRequiredMixin,CreateView): #book_form.html
    model = Book 
    fields = '__all__'

class BookDetail(DetailView):
    model = Book


# authentication for function based views
# login required makes sure u r loggedin 
# if u hit http://127.0.0.1:8080/FirstApp/my_view it redirects to
# # http://127.0.0.1:8080/accounts/login/?next=/FirstApp/my_view/ 
@login_required 
def my_view(request):
    return render(request,'FirstApp/my_view.html')





class SignUpView(CreateView):
    form_class = UserCreationForm  # as we are using UserCreation Form
    # it automatically send the form earlier incase of BookCreate it sends the form from Book Model.
    success_url = reverse_lazy('login')
    # login is not present in urls.py but i dont have to worruy about it as we are also using it in login.html url:login
    # it is built in to django
    template_name = 'FirstApp/signup.html'
    # as it is create view it automatically looks  for model_form.html , but we are overiding with UserCreationForm
    # we are overriding template_name with  'FirstApp/signup.html'



class CheckedOutBooksByUserView(LoginRequiredMixin,ListView):
    # List all BookInstances BUT I will filter based off currently logged in user session
    model = BookInstance 
    template_name = 'FirstApp/profile.html'
    paginate_by = 5 # 5 book instances per page

    # for listView the default is just to query every single book instance
    # to override that behaviour we have to define get_queryset
    def get_queryset(self):
        #print(self.request) # prints <WSGIRequest: GET '/FirstApp/profile/'>
        return BookInstance.objects.filter(borrower=self.request.user) 
