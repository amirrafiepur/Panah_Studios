# Create your views here.

from django.shortcuts import render
from webb.models import Human
from webb.forms import add_human


def index(request):
    table_data=Human.objects.all()
    my_dic={"data" : table_data}
    return render(request,'webb/index.html',context=my_dic)

def index_addHuman(request):
    if request.method=='POST':
        form=add_human()
        form=add_human(request.POST)
        form.save(commit=True)
        return index(request)
    else:
        form=add_human()
    return render(request,'webb/forms.html',context={'form':form}) 