from django.shortcuts import render , get_object_or_404
from blog.models import post

def blog_home(request,cat_name=None,author_name=None):
    posts=post.objects.filter(status=1)
    if cat_name:
        posts=posts.filter(post_category__name=cat_name)
        context={'datas':posts}
        return render(request,'blog/blog-home.html',context)
    elif author_name:
        posts=posts.filter(author__username=author_name)
        context={'datas':posts}
        return render(request,'blog/blog-home.html',context)
    else:
        context={'datas': posts }
        return render(request,'blog/blog-home.html',context)

def blog_single(request,pid):
    context={'data' : get_object_or_404(post , id=pid , status=1)}
    return render(request,'blog/blog-single.html', context)