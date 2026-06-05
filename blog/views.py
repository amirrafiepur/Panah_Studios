from django.shortcuts import render , get_object_or_404
from blog.models import post

def blog_home(request):
    context={'datas' : post.objects.all()}
    return render(request,'blog/blog-home.html',context)

def blog_single(request,pid):
    context={'data' : get_object_or_404(post , id=pid , status=1)}
    return render(request,'blog/blog-single.html', context)

