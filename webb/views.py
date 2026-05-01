# Create your views here.

from django.shortcuts import render
from webb.models import Human


def index(request):
    table_data=Human.objects.all()
    my_dic={"data" : table_data}
    return render(request,'webb/index.html',context=my_dic)