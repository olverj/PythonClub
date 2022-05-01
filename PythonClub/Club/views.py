from django.shortcuts import render
from .models import Meeting, Resource

# Create your views here.
def index(request):
    return render(request, 'Club/index.html')

def meeting(request):
    meetingtitle=Meeting.objects.all()
    return render(request, 'Club/meetings.html', {'meetingtitle': meetingtitle})

def clubresources(request):
    resourcename=Resource.objects.all()
    return render(request, 'Club/resources.html', {'resourcename': resourcename})
