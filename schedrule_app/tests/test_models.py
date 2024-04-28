from django.utils import timezone
from django.test import TestCase
from schedrule_app.models import Event,EventType
from django.urls import reverse

class EventModelTests(TestCase):
    def setUp(self):
        self.event_type = EventType.objects.create(name='Meeting')
        self.event = Event.objects.create(
            type=self.event_type,
            name='Team Meeting',
            start_date_time=timezone.now(),
            end_date_time=timezone.now() + timezone.timedelta(hours=1),
            description='Test description'
        )

    def test_event_creation(self):
        self.assertEqual(self.event.type, self.event_type)
        self.assertEqual(self.event.name, 'Team Meeting')
        self.assertIsNotNone(self.event.start_date_time)
        self.assertIsNotNone(self.event.end_date_time)
        self.assertEqual(self.event.description, 'Test description')

    def test_event_str_method(self):
        self.assertEqual(str(self.event), 'Team Meeting')

    def test_get_absolute_url(self):
        expected_url = reverse('event-detail', args=[str(self.event.id)])
        self.assertEqual(self.event.get_absolute_url(), expected_url)
