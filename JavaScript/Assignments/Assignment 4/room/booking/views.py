import secrets

from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render

from .forms import BookingForm, SearchForm
from .models import Booking, Classroom
from .services import available_classrooms, classroom_is_available


def home(request):
    form = SearchForm(request.GET or None)
    classrooms = None
    searched = False
    if form.is_valid() and form.cleaned_data:
        searched = True
        classrooms = available_classrooms(**form.cleaned_data)
    return render(request, 'booking/home.html', {'form': form, 'classrooms': classrooms, 'searched': searched})


def reserve(request, classroom_id):
    classroom = get_object_or_404(Classroom, pk=classroom_id, is_active=True)
    initial = {
        'check_in': request.GET.get('check_in'),
        'check_out': request.GET.get('check_out'),
        'guests': request.GET.get('guests', 2),
    }
    form = BookingForm(request.POST or None, initial=initial)
    if request.method == 'POST' and form.is_valid():
        data = form.cleaned_data
        with transaction.atomic():
            classroom = Classroom.objects.select_for_update().get(pk=classroom_id)
            if not classroom_is_available(classroom, data['check_in'], data['check_out'], data['guests']):
                form.add_error(None, 'Sorry, this classroom was just booked for those dates. Please choose another classroom.')
            else:
                booking = Booking.objects.create(
                    classroom=classroom,
                    confirmation_code=f'CB-{secrets.token_hex(4).upper()}',
                    **data,
                )
                return redirect('booking:confirmation', code=booking.confirmation_code)
    return render(request, 'booking/reserve.html', {'classroom': classroom, 'form': form})


def confirmation(request, code):
    booking = get_object_or_404(Booking.objects.select_related('classroom'), confirmation_code=code)
    return render(request, 'booking/confirmation.html', {'booking': booking})
