from django.urls import path
from . import views
urlpatterns = [
   path('', views.index, name='index'),
   path('meetings/', views.meeting, name='meeting'),
   path('resources/', views.clubresources, name='clubresources'),
   path('meetingdetail/<int:id>', views.meetingdetail, name='meetingminutes'),
   path('newmeeting/', views.newMeeting, name = 'newmeeting'),
   path('newresource/', views.newResource, name = 'newresource'),
   path('resourcedetail/<int:id>', views.resourcedetail, name = 'resourcedetails')
   ]