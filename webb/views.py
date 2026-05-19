# Create your views here.

from django.shortcuts import render
from webb.models import Human  #TODO:add a table in index.html to show the table Human in database


def index(request):
    return render(request,'webb/index.html')

def back(request):
    return render(request,'webb/back.html')

def front(request):
    return render(request,'webb/front.html')

def contact(request):
    return render(request,'webb/contact.html')



def index_portfolio_kenburns(request):
    return render(request,'webb/index-portfolio-kenburns.html')

def index_countdown_slider(request):
    return render(request,'webb/index-countdown-slider.html')

def index_agency_video(request):
    return render(request,'webb/index-agency-video.html')
