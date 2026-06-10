from django import template 
from blog.models import * 
register = template.Library()

@register.simple_tag
def tag_name():
    return 'This is a simple tag'

@register.filter
def filter_tag(data): 
    return 3 + data

@register.inclusion_tag('blog/test.html')
def inclusion_tag():
    posts = post.objects.filter(status=1)
    return {'posts':posts}