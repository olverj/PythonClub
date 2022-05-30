from django.test import TestCase
from django.contrib.auth.models import User
from django.forms import URLField
from .models import Meeting, MeetingMinutes, Resource, Event
from django.urls import reverse, reverse_lazy
import datetime
from .forms import MeetingForm, ResourceForm

# Create your tests here.
class MeetingNameTest(TestCase):
    def setUp(self):
        self.meet = Meeting(meetingtitle = 'Bird Meeting')

    def test_meetstring(self):
        self.assertEqual(str(self.meet), 'Bird Meeting')

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class MeetingMinutesTest(TestCase):
    def setUp(self):
        self.min = MeetingMinutes(minutestext = 'All birds present')

    def test_minstring(self):
        self.assertEqual(str(self.min), 'All birds present')

    def test_tablename(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'meetingminutes')

class MinutesTest(TestCase):
    def setUp(self):
        self.user = User(username = 'Crow')
        self.meeting = Meeting.objects.create(
            meetingtitle = 'Flight practice',
            meetingdate = datetime.date(2022,4,20),
            meetingtime = datetime.time(6,00),
            meetinglocation = 'Seward Park',
            meetingagenda = 'Practice flying'
        )
        self.text = MeetingMinutes(minutestext = 'Flight practice tomorrow')
    
    def test_Meeting_with_Minutes(self):
        response = self.client.get(reverse('meeting'), args = (self.meeting.id))
        self.assertEqual(response.status_code, 200)

class ResourceNameTest(TestCase):
    def setUp(self):
        self.resource = Resource(resourcename = 'How to be a bird')
    
    def test_resourcestring(self):
        self.assertEqual(str(self.resource), 'How to be a bird')
    
    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class ResourceTest(TestCase):
    def setUp(self):
        self.type = Resource(resourcetype = 'SOP')
        self.user = User(username = 'Pigeon')
        self.resource = Resource(
            resourcename = 'How to be a bird',
            resourceurl = 'http://www.pigeon101.com',
            resourcedate = datetime.date(2022,1,1),
            user = self.user,
            resourcedescription = 'Everything you need to know about being a bird'
        )
    
    def test_string(self):
        self.assertEqual(str(self.resource), 'How to be a bird')

class ResourceURLTest(TestCase):
    def test_urlerror(self):
        self.assertFieldOutput(URLField, {'http://www.pigeon101.com' : 'http://www.pigeon101.com'},
            {'pigeon' : ['Enter a valid URL.']})

class EventTitleTest(TestCase):
    def setUp(self):
        self.event = Event(eventtitle = 'Flight practice')
    
    def test_eventstring(self):
        self.assertEqual(str(self.event), 'Flight practice')
    
    def test_tablename(self):
        self.assertEqual(str(Event._meta.db_table), 'event')

class NewMeetingForm(TestCase):
    def test_meetingform(self):
        data = {
            'meetingtitle' : 'hiring new staff',
            'meetingdate' : '2022-02-22',
            'meetingtime' : '12:00',
            'meetinglocation' : 'Room 400',
            'meetingagenda' : 'guidance for hiring new staff'
        }
        form = MeetingForm(data)
        self.assertTrue(form.is_valid)

class NewResourceForm(TestCase):
    def test_resourceform(self):
        data = {
            'resourcename' : 'python security',
            'resourcetype' : 'SOP',
            'resourceurl' : 'https://www.python.org',
            'resourcedate' : '2022-05-18',
            'user' : 'saki',
            'resourcedescription' : 'security protocols for python'
        }
        form = ResourceForm(data)
        self.assertTrue(form.is_valid)

class NewResAuthTest(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username = 'testuser1', password = 'password')
        self.res = Resource.objects.create(
            resourcename = 'python security',
            resourcetype = 'SOP',
            resourceurl = 'https://www.python.org',
            resourcedate = '2022-05-18',
            user = self.test_user,
            resourcedescription = 'security protocols for python'
        )
    
    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('newresource'))
        self.assertRedirects(response, '/accounts/login/?next=/Club/newresource/')

class LoginTest(TestCase):
    def test_login_template(self):
        response = self.client.get(reverse('loginmessage'))
        self.assertTemplateUsed(response, 'Club/loginmessage.html')

