# -*- coding: utf-8 -*-
from django.test import TestCase, Client, RequestFactory
from agenda.models import Event
import datetime
from django.utils.encoding import smart_text
from .views import index

ENG_TEXT = """Lorem ipsum dolor sit amet,consectetur adipiscing elit.
Praesent nec enim in erat fermentum feugiat a sit amet nisi.
Cras tempor nisl ac quam commodo, ut pharetra sapien ultricies."""


POL_TEXT = """Litwo! Ojczyzno moja! Ty jesteś jak zdrowie.
Ile cię trzeba cenić, ten tylko się spory o jej ubrani wysmukłą postać tylko
cichy smutek panów groni mają od obywateli."""


class EventDatabaseTest(TestCase):
    def setUp(self):
        Event.objects.create(id=1, title='Lorem ipsum', start_time='15:55:55',
                             end_time='16:55:55', desc=ENG_TEXT,
                             prelector='John Smith', classroom='A')
        Event.objects.create(id=2, title='Świerzop', start_time='12:00:12',
                             end_time='12:30:22', desc=POL_TEXT,
                             prelector='Grzegorz Brzęczyszczykiewicz', classroom='32')

    def test_events_have_start_end_times(self):
        first_event = Event.objects.get(id=1)
        second_event = Event.objects.get(id=2)
        self.assertEqual(first_event.start_time, datetime.time(15, 55, 55))
        self.assertEqual(first_event.end_time, datetime.time(16, 55, 55))
        self.assertEqual(second_event.start_time, datetime.time(12, 00, 12))
        self.assertEqual(second_event.end_time, datetime.time(12, 30, 22))

    def test_events_have_title(self):
        first_event = Event.objects.get(id=1)
        second_event = Event.objects.get(id=2)
        self.assertEqual(first_event.title, 'Lorem ipsum')
        self.assertEqual(second_event.title, smart_text('Świerzop'))

    def test_events_have_desc(self):
        first_event = Event.objects.get(id=1)
        second_event = Event.objects.get(id=2)
        self.assertEqual(first_event.desc, ENG_TEXT)
        self.assertEqual(second_event.desc, smart_text(POL_TEXT))

    def test_events_have_prelector(self):
        first_event = Event.objects.get(id=1)
        second_event = Event.objects.get(id=2)
        self.assertEqual(first_event.prelector, 'John Smith')
        self.assertEqual(second_event.prelector, smart_text('Grzegorz Brzęczyszczykiewicz'))

    def test_events_have_classroom(self):
        first_event = Event.objects.get(id=1)
        second_event = Event.objects.get(id=2)
        self.assertEqual(first_event.classroom, 'A')
        self.assertEqual(second_event.classroom, '32')


class EventViewsTest(TestCase):
    def setUp(self):
        Event.objects.create(id=1, title='Lorem ipsum', start_time='15:55:55',
                             end_time='16:55:55', desc=POL_TEXT,
                             prelector='John Smith', classroom='A')
        self.event_factory = Event.objects.create(title='Factory test', start_time='10:00:01',
                                                  end_time='11:00:00', desc='Simple factory test',
                                                  prelector='Factory', classroom='F')
        self.client = Client()
        self.factory = RequestFactory()

    def test_index_view_get_with_client(self):
        response = self.client.get('/agenda/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data['events'][0].start_time, datetime.time(15, 55, 55))
        self.assertEqual(response.context_data['events'][0].end_time, datetime.time(16, 55, 55))
        self.assertEqual(response.context_data['events'][0].title, 'Lorem ipsum')
        self.assertEqual(response.context_data['events'][0].desc, smart_text(POL_TEXT))
        self.assertEqual(response.context_data['events'][0].prelector, 'John Smith')
        self.assertEqual(response.context_data['events'][0].classroom, 'A')

    def test_index_view_get_with_request_factory(self):
        request = self.factory.get('/agenda/')
        request.event = self.event_factory
        response = index(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context_data['events'][1].start_time, datetime.time(10, 00, 01))
        self.assertEqual(response.context_data['events'][1].end_time, datetime.time(11,00,00))
        self.assertEqual(response.context_data['events'][1].title, 'Factory test')
        self.assertEqual(response.context_data['events'][1].desc, 'Simple factory test')
        self.assertEqual(response.context_data['events'][1].prelector, 'Factory')
        self.assertEqual(response.context_data['events'][1].classroom, 'F')