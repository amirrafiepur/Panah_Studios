# Create your views here.

from django.shortcuts import render
from webb.models import Human  #TODO:add a table in index.html to show the table Human in database


def index(request):
    return render(request,'webb/index.html')
def index_portfolio_kenburns(request):
    return render(request,'webb/index-portfolio-kenburns.html')
def index_portfolio_image(request):
    return render(request,'webb/index-portfolio-image.html')
def index_countdown_slider(request):
    return render(request,'webb/index-countdown-slider.html')
def index_countdown_particles_image(request):
    return render(request,'webb/index-countdown-particles-image.html')
def index_agency_video(request):
    return render(request,'webb/index-agency-video.html')
def index_agency_triangles_slider(request):
    return render(request,'webb/index-agency-triangles-slider.html')