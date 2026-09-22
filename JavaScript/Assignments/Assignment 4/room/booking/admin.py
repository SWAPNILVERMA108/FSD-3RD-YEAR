from django.contrib import admin

from .models import Booking, Classroom


@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'classroom_type', 'capacity', 'rate_per_day', 'is_active')
    list_filter = ('classroom_type', 'is_active')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('confirmation_code', 'guest_name', 'classroom', 'check_in', 'check_out', 'status')
    list_filter = ('status',)
    search_fields = ('confirmation_code', 'guest_name', 'guest_email')
