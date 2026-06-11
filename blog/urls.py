from django.urls import path
from blog.views import *

app_name="blog"

urlpatterns = [
    path('',blog_home,name='blog'),
    path('<int:pid>',blog_single,name='single'),
    path('category/<str:cat_name>',blog_home,name='blog_category'),
    path('<str:author_name>',blog_home,name='author'),
    
] 
