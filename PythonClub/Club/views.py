from django.shortcuts import render, get_object_or_404
from .models import Meeting, Resource
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request, 'Club/index.html')

def meeting(request):
    meetingtitle=Meeting.objects.all()
    return render(request, 'Club/meetings.html', {'meetingtitle': meetingtitle})

def meetingdetail(request, id):
    meet=get_object_or_404(Meeting, id=id)
    meetingtitle=meet.meetingtitle
    meetingdate=meet.meetingdate
    meetingtime=meet.meetingtime
    meetinglocation=meet.meetinglocation
    meetingagenda=meet.meetingagenda
    context={
        'meet' : meet,
        'meetingtitle' : meetingtitle,
        'meetingdate' : meetingdate,
        'meetingtime' : meetingtime,
        'meetinglocation' : meetinglocation,
        'meetingagenda' : meetingagenda,
    }
    return render(request, 'Club/meetingdetail.html', context)

def clubresources(request):
    resourcename=Resource.objects.all()
    return render(request, 'Club/resources.html', {'resourcename': resourcename})
