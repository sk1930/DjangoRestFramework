from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

# creating dynamic views and urlpatterns here


'''
def  news_view(request):
    return HttpResponse("Sport Page")

    
this is converted as below
'''
articles = {
    'sports': 'sports page',
    'finance': 'finance page',
    'politics': 'politics page'
}

# http://127.0.0.1:8000/secondapp/sports
def  news_view(request,topic):
    try:
        result = articles[topic]
        return HttpResponse(result)
    except:
        '''
        result='No page for that topic'
        # now if request is like http://127.0.0.1:8000/secondapp/abcd
        # response is like No page for that topic
        return HttpResponseNotFound(result)
        '''
        # instead of HttpResponseNotFound u can also do Http404 genertic error

        ''' to see the error page properly in settings.py set Debug= False and allowed hosts = ["127.0.0.1"] '''
        raise Http404("404 GENERIC ERROR")

# http://127.0.0.1:8000/secondapp/3/4
def addition_view(request,num1,num2):
    summ=num1+num2
    result=f"{num1}+{num2}={summ}"
    return HttpResponse(result)



# url redirecting

# http://127.0.0.1:8000/secondapp/0 --> # http://127.0.0.1:8000/secondapp/sports

'''
def num_page_view(request,num_page):
    topics_list = list(articles.keys())
    topic = topics_list[num_page]
    return HttpResponseRedirect(topic)

    this is using the HttpResponseRedirect with the topic by using reverse itmakes more efficient

'''
'''    path('<str:topic>',views.news_view,name='topic_page'),
named it as topic page to be used in reverese
'''
# http://127.0.0.1:8000/secondapp/0

def num_page_view(request,num_page):
    topics_list = list(articles.keys())
    topic = topics_list[num_page]
    webpage = reverse('topic_page',args=[topic]) # topic_page url has topic argument
    return HttpResponseRedirect(webpage)
