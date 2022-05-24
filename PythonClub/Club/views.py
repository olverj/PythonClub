from django.shortcuts import render, get_object_or_404
from .models import Meeting, Resource
from django.urls import reverse_lazy
from .forms import MeetingForm, ResourceForm
from django.contrib.auth.decorators import login_required

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

@login_required
def newMeeting(request):
    form = MeetingForm

    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            post = form.save(commit = True)
            post.save()
            form = MeetingForm()
    else:
        form = MeetingForm()
    return render(request, 'club/newmeeting.html', {'form' : form})

def resourcedetail(request, id):
    res=get_object_or_404(Resource, id=id)
    resourcename = res.resourcename
    resourcetype = res.resourcetype
    resourceurl = res.resourceurl
    resourcedate = res.resourcedate
    user = res.user
    resourcedescription = res.resourcedescription
    context={
        'res' : res,
        'resourcename' : resourcename,
        'resourcetype' : resourcetype,
        'resourceurl' : resourceurl,
        'resourcedate' : resourcedate,
        'user' : user,
        'resourcedescription' : resourcedescription,
    }
    return render(request, 'Club/resourcedetail.html', context)

@login_required
def newResource(request):
    form = ResourceForm

    if request.method == 'POST':
        form = ResourceForm(request.POST)
        if form.is_valid():
            post = form.save(commit = True)
            post.save()
            form = ResourceForm()
    else:
        form = ResourceForm()
    return render(request, 'club/newresource.html', {'form' : form})

def loginmessage(request):
    return render(request, 'Club/loginmessage.html')

def logoutmessage(request):
    return render(request, 'Club/logoutmessage.html')