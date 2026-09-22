from django.core.validators import MinValueValidator
from django.db import models


class Classroom(models.Model):
    class ClassroomType(models.TextChoices):
        LECTURE_HALL = 'lecture', 'Lecture Hall'
        COMPUTER_LAB = 'computer', 'Computer Lab'
        SEMINAR_ROOM = 'seminar', 'Seminar Room'

    number = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=80)
    classroom_type = models.CharField(max_length=20, choices=ClassroomType.choices)
    capacity = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    rate_per_day = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.CharField(max_length=180)
    amenities = models.CharField(max_length=240)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['rate_per_day', 'number']

    def __str__(self):
        return f'{self.number} — {self.name}'


class Booking(models.Model):
    class Status(models.TextChoices):
        CONFIRMED = 'confirmed', 'Confirmed'
        CANCELLED = 'cancelled', 'Cancelled'

    classroom = models.ForeignKey(Classroom, on_delete=models.PROTECT, related_name='bookings')
    guest_name = models.CharField(max_length=100)
    guest_email = models.EmailField()
    guests = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    check_in = models.DateField()
    check_out = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    confirmation_code = models.CharField(max_length=14, unique=True)
    status = models.CharField(max_length=12, choices=Status.choices, default=Status.CONFIRMED)

    class Meta:
        ordering = ['-created_at']

    @property
    def nights(self):
        return (self.check_out - self.check_in).days

    @property
    def total(self):
        return self.classroom.rate_per_day * self.nights

    def __str__(self):
        return f'{self.confirmation_code} — {self.guest_name}'
