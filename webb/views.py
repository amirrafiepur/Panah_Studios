# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    my_dic={'name':"amir"}
    return render(request,'webb/index.html',context=my_dic)