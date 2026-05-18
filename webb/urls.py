from django.urls import path
from webb.views import *



urlpatterns = [
    path('',index,name='index'),
] 
