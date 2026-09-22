from datetime import date

from django.test import TestCase

from .models import Booking, Classroom
from .services import available_classrooms, classroom_is_available


class AvailabilityTests(TestCase):
    def setUp(self):
        self.classroom = Classroom.objects.create(number='T1', name='Test Classroom', classroom_type='seminar', capacity=2, rate_per_day=1000, description='Test', amenities='Projector')
        Booking.objects.create(classroom=self.classroom, guest_name='A Guest', guest_email='guest@example.com', guests=2, check_in=date(2026, 10, 10), check_out=date(2026, 10, 14), confirmation_code='CB-TEST0001')

    def test_overlapping_stay_is_not_available(self):
        self.assertFalse(classroom_is_available(self.classroom, date(2026, 10, 12), date(2026, 10, 16), 2))
        self.assertFalse(available_classrooms(date(2026, 10, 12), date(2026, 10, 16), 2).filter(pk=self.classroom.pk).exists())

    def test_back_to_back_stay_is_available(self):
        self.assertTrue(classroom_is_available(self.classroom, date(2026, 10, 14), date(2026, 10, 16), 2))

    def test_room_cannot_be_booked_above_capacity(self):
        self.assertFalse(classroom_is_available(self.classroom, date(2026, 10, 15), date(2026, 10, 16), 3))
