from django.urls import path
from . import views

'''
urlpatterns=[
    path('<topic>',views.news_view)    
]
this can be also written as      path('<str:topic>',views.news_view),

'''


'''
    path('<int:num_page>',views.num_page_view) should be above the str:num_page
    becoz in url if we pass 0 it will be first hit the int one next when redirect happens it automatically hits the 
    string one

    but if str is first then 
    # http://127.0.0.1:8000/secondapp/0  this will hit the str:topic view and it will fail

'''
urlpatterns=[
    path('<int:num_page>',views.num_page_view),
    path('<str:topic>',views.news_view,name='topic_page'),

    path('<int:num1>/<int:num2>',views.addition_view)    
]    



''' if the url is just passed as 
http://127.0.0.1:8000/secondapp/

error page shows 
Using the URLconf defined in FirstDjangoProject.urls, Django tried these URL patterns, in this order:

admin/
firstapp/
secondapp/ <topic>
The current path, secondapp/, didn’t match any of these.


So pass http://127.0.0.1:8000/secondapp/sports
'''