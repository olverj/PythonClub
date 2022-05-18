from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Meeting(models.Model):
    meetingtitle=models.CharField(max_length=255)
    meetingdate=models.DateField(null=True, blank=True)
    meetingtime=models.TimeField(null=True, blank=True)
    meetinglocation=models.TextField(max_length=255)
    meetingagenda=models.TextField(null=False)

    def __str__(self):
        return self.meetingtitle

    class Meta:
        db_table='meeting'

class MeetingMinutes(models.Model):
    meetingid=models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    minutestext=models.TextField(null=False)

    def __str__(self):
        return self.minutestext

    class Meta:
        db_table='meetingminutes'

class Resource(models.Model):
    resourcename=models.CharField(max_length=255)
    resourcetype=models.TextField()
    resourceurl=models.URLField(null=True, blank=True)
    resourcedate=models.DateField(null=True, blank=True)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    resourcedescription=models.TextField(null=False)

    def __str__(self):
        return self.resourcename

    class Meta:
        db_table='resource'

class Event(models.Model):
    eventtitle=models.CharField(max_length=255)
    eventlocation=models.TextField(null=False)
    eventdate=models.DateField(null=True, blank=True)
    eventtime=models.TimeField(null=True, blank=True)
    eventdescription=models.TextField(blank=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.eventtitle
    
    class Meta:
        db_table='event'