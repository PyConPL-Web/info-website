# -*- coding: utf-8 -*-
from django.test import TestCase
from agenda.models import Event
import datetime
from django.utils.encoding import smart_text

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

    #  this test should fail
    def test_events_start_time_after_end_time(self):
        Event.objects.create(id=3, title='Time', start_time='15:55:55',
                             end_time='10:55:55', desc='Time is money',
                             prelector='Mr Time', classroom='T')
