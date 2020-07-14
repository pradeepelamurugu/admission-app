from django.urls import path
from . import views
urlpatterns = [
    path('staff/', views.staff_view , name='staff_view'),
    path('staffselected/', views.staff_accept_view , name='staff_accept_view'),


    ]