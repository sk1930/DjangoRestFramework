from django.shortcuts import render
from django.views.generic import TemplateView,FormView,CreateView,ListView,DetailView,UpdateView, DeleteView
from django.urls import reverse_lazy
from . import forms
from . import models

# Create your views here.


#http://127.0.0.1:8080/FirstApp
# this is the function based view
def home_view(request):
    return render(request,'FirstApp/home.html')


#http://127.0.0.1:8080/FirstApp/thankyou

# this is the class based view
class ThankYouView(TemplateView):
    # connecting to the html file 
    template_name = 'FirstApp/thankyou.html'
    #now we have to connect this to urls.py
    #and urls.py needs a function 
    # ThankYouView.as_view() in urls.py 


# this is form view
class ContactFormView(FormView):
    form_class = forms.ContactForm
        # connecting to the html file 
    template_name = 'FirstApp/contact.html'

    # success URL? 
    ''' u can directly use as below or u can also use reverse lazy
    success_url = "/FirstApp/thankyou/"'''
    success_url = reverse_lazy("FirstApp:thankyou")

    #what to do with form
    # this is with request==POST
    def form_valid(self,form):
        print(form.cleaned_data)
        # https://docs.djangoproject.com/en/4.1/topics/class-based-views/generic-editing/
        # below line is with inheritance we are calling FormView.form_valid()
        # The default implementation for form_valid() simply redirects to the success_url.
        # AM not sure if this really has a validation i think we have to do the validation here
        # 
        return super().form_valid(form)
        '''def form_valid(self, form):
        """If the form is valid, redirect to the supplied URL."""
        return HttpResponseRedirect(self.get_success_url())'''

#http://127.0.0.1:8080/FirstApp/

class TeacherCreateView(CreateView):
    model = models.Teacher  # it is not Teacher()
    # as we have given the model it automatically looks for the template Teacher_form.hmtl
    # fields to be displayed on the create form
    fields = "__all__" # or u can give  a list []
    # it automatically calls .save() on the model on click of submit
    success_url = reverse_lazy("FirstApp:thankyou")


#http://127.0.0.1:8080/FirstApp/
class TeacherListView(ListView):
    model = models.Teacher  # it is not Teacher()

    context_object_name ="teacher_list"
    # if context_object name isnot  specified 
    # {% for teacher in object_list   %}     
    #    by default it is object_list
    #but if u specify any context_object_name then use that here 
    #like context_object_name ="teacher_list"-->
    # #<ul>{% for teacher in  teacher_list %}
    
    
    # u need not specify the queryset
    # it is by default queryset = Teacher.objects.all()
    # but u can override
    queryset = models.Teacher.objects.order_by('first_name')
  
# goto http://127.0.0.1:8080/FirstApp/
# add some records and goto list and then click on each teacher link to goto detailed view
class TeacherDetailView(DetailView):
    model = models.Teacher  # it is not Teacher()
    # for a specific primary key of a teacher
    # pk --> {{teacher}}


class TeacherUpdateView(UpdateView):
    # it share model_form.html that create view uses ---- Primary key 
    model = models.Teacher  # it is not Teacher()
    fields = "__all__" # or u can have a list of fields for update
    success_url = reverse_lazy("FirstApp:thankyou")

class TeacherDeleteView(DeleteView):
    # form -- single confirm delete button
    # it looks for model_confirm _delete.html
    model = models.Teacher
    success_url = reverse_lazy("FirstApp:list_teacher")



