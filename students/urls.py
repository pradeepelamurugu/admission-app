from django.urls import path
from . import views
urlpatterns = [
    path('createstudent/', views.student_create_view , name='student_create'),
    path('',views.welcome,name='welcome')
]