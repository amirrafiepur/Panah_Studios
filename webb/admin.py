# Register your models here.

from django.contrib import admin
from webb.models import *
from blog.models import *

admin.site.register(Human)
admin.site.register(tags)
admin.site.register(category)
admin.site.register(comments)

class webbAdmin(admin.ModelAdmin):
    list_display=['title','status']
    search_fields=['title','comment','body']

admin.site.register(post,webbAdmin)