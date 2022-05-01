from django.urls import path
from . import views
urlpatterns = [
   path('', views.index, name='index'),
   path('meetings/', views.meeting, name='meetings'),
   path('resources/', views.clubresources, name='resources')
   ]