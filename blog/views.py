from django.shortcuts import render , get_object_or_404
from blog.models import post

def blog_home(request,**kwargs):
    posts=post.objects.filter(status=1)
    if kwargs.get('cat_name')!=None:
        posts=posts.filter(post_category__name=kwargs['cat_name'])
        context={'datas':posts}
        return render(request,'blog/blog-home.html',context)
    elif kwargs.get('author_name')!=None:
        posts=posts.filter(author__username=kwargs['author_name'])
        context={'datas':posts}
        return render(request,'blog/blog-home.html',context)
    else:
        context={'datas': posts }
        return render(request,'blog/blog-home.html',context)

def blog_single(request,pid):
    context={'data' : get_object_or_404(post , id=pid , status=1)}
    return render(request,'blog/blog-single.html', context)

def blog_search(request):
    posts=post.objects.filter(status=1)
    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts=posts.filter(body__contains=s)
            context={'datas' : posts}
            return render(request,'blog/blog-home.html',context)
    context={'datas' : posts}
    return render(request,'blog/blog-home.html',context)