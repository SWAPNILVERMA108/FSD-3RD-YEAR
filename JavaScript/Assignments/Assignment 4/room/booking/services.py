from .models import Booking, Classroom


def available_classrooms(check_in, check_out, guests):
    """A stay overlaps when it starts before an existing checkout and ends after its check-in."""
    conflicts = Booking.objects.filter(
        classroom__is_active=True,
        status=Booking.Status.CONFIRMED,
        check_in__lt=check_out,
        check_out__gt=check_in,
    ).values('classroom_id')
    return Classroom.objects.filter(is_active=True, capacity__gte=guests).exclude(id__in=conflicts)


def classroom_is_available(classroom, check_in, check_out, guests):
    return classroom.is_active and classroom.capacity >= guests and not Booking.objects.filter(
        classroom=classroom,
        status=Booking.Status.CONFIRMED,
        check_in__lt=check_out,
        check_out__gt=check_in,
    ).exists()
