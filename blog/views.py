from django.shortcuts import render
from blog.models import post

def blog_home(request):
    context={'datas' : post.objects.all()}
    return render(request,'blog/blog-home.html',context)

def blog_single(request):
    return render(request,'blog/blog-single.html')