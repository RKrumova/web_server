from django.contrib import admin

# Register your models here.
from .models import Holiday, Location, Reservation

@admin.register(Holiday)
class HolidayAdmin(admin.ModelAdmin):
    list_display = ['id', 'location', 'title', 'start_date', 'duration', 'price', 'free_slots']

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['id', 'street', 'number', 'city', 'country', 'image_url']

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['id', 'contact_name', 'phone_number', 'holiday']
