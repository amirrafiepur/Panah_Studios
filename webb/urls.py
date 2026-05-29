from django.urls import path
from webb.views import *

app_name="webb"

urlpatterns = [
    path('',index,name='home'),
    path('contact/',contact,name="contact"),
    path('front-end/',front,name='front'),
    path('back-end/',back,name='back')
] 
