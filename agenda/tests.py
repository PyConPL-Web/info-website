# -*- coding: utf-8 -*-
from django.test import TestCase, Client, RequestFactory
from agenda.models import Event
import datetime
from django.utils.encoding import smart_text
from .views import index
from django.core.urlresolvers import reverse

ENG_TEXT = """Lorem ipsum dolor sit amet,consectetur adipiscing elit.
Praesent nec enim in erat fermentum feugiat a sit amet nisi.
Cras tempor nisl ac quam commodo, ut pharetra sapien ultricies."""


POL_TEXT = """Litwo! Ojczyzno moja! Ty jesteś jak zdrowie.
Ile cię trzeba cenić, ten tylko się spory o jej ubrani wysmukłą postać tylko
cichy smutek panów groni mają od obywateli."""


class EventDatabaseTest(TestCase):
    def setUp(self):
        Event.objects.create(id=1, title='Lorem ipsum', date='2015-4-1', start_time='15:55:55',
                             end_time='16:55:55', desc=ENG_TEXT,
                             prelector='John Smith', classroom='A')
        Event.objects.create(id=2, title='Świerzop', date='2015-4-2', start_time='12:00:12',
                             end_time='12:30:22', desc=POL_TEXT,
                             prelector='Grzegorz Brzęczyszczykiewicz', classroom='32')
        self.first_event = Event.objects.get(id=1)
        self.second_event = Event.objects.get(id=2)

    def test_events_have_start_end_times(self):
        self.assertEqual(self.first_event.start_time, datetime.time(15, 55, 55))
        self.assertEqual(self.first_event.end_time, datetime.time(16, 55, 55))
        self.assertEqual(self.second_event.start_time, datetime.time(12, 00, 12))
        self.assertEqual(self.second_event.end_time, datetime.time(12, 30, 22))

    def test_events_have_title(self):
        self.assertEqual(self.first_event.title, 'Lorem ipsum')
        self.assertEqual(self.second_event.title, smart_text('Świerzop'))

    def test_events_have_desc(self):
        self.assertEqual(self.first_event.desc, ENG_TEXT)
        self.assertEqual(self.second_event.desc, smart_text(POL_TEXT))

    def test_events_have_prelector(self):
        self.assertEqual(self.first_event.prelector, 'John Smith')
        self.assertEqual(self.second_event.prelector, smart_text('Grzegorz Brzęczyszczykiewicz'))

    def test_events_have_classroom(self):
        self.assertEqual(self.first_event.classroom, 'A')
        self.assertEqual(self.second_event.classroom, '32')

    def test_model_methods(self):
        self.assertEqual(self.first_event.get_start_time(), 70)
        self.assertEqual(self.first_event.get_end_time(), 71)
        self.assertEqual(self.first_event.get_end_time() - self.first_event.get_start_time(), 1)


class EventViewsTest(TestCase):
    def setUp(self):
        Event.objects.create(id=1, title='Lorem ipsum', date='2015-4-3', start_time='15:55:55',
                             end_time='16:55:55', desc=POL_TEXT,
                             prelector='John Smith', classroom='A')
        self.event_factory = Event.objects.create(title='Factory test', date='2015-4-3', start_time='10:00:01',
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

    def test_detail_view(self):
        response = self.client.get('/agenda/detail/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Lorem ipsum')
        self.assertContains(response, smart_text(POL_TEXT))
        request = self.factory.get('/agenda/detail/2/')
        request.event = self.event_factory
        response_1 = index(request)
        self.assertEqual(response_1.status_code, 200)
        self.assertContains(response_1, 'Factory test')
        self.assertEqual(response_1.context_data['events'][1].desc, 'Simple factory test')