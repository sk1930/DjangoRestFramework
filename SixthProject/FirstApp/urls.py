from django.urls import path
from . import views
# we can also write this as from .views import TahnkYouView,ContactFormView,...TeacherDeleteView

app_name='FirstApp'

urlpatterns = [
    path('',views.home_view,name='home'),
    path('thankyou/',views.ThankYouView.as_view(),name='thankyou'),
    path('contact/',views.ContactFormView.as_view(),name='contact'),
    path('create_teacher/',views.TeacherCreateView.as_view(),name='create_teacher'),
    path('list_teacher/',views.TeacherListView.as_view(),name='list_teacher'),
    path('teacher_detail/<int:pk>',views.TeacherDetailView.as_view(),name='detail_teacher'),
    path('teacher_update/<int:pk>',views.TeacherUpdateView.as_view(),name='teacher_update'),
    path('teacher_delete/<int:pk>',views.TeacherDeleteView.as_view(),name='teacher_delete'),

]