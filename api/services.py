from .models import Location, Holiday, Reservation
from django.http import JsonResponse
from django.core import serializers
from rest_framework import status
from .serializers import LocationSerializer, HolidaySerializer, ReservationSerializer
from datetime import datetime


def create_location(request):
    number = request.data.get('number')
    country = request.data.get('country')
    city = request.data.get('city')
    image_url = request.data.get('image_url')
    
    try:
        location = Location(
            number=number,
            country=country,
            city=city,
            image_url=image_url,
        )
        location.save()
        return {'Success': 'Location was created'}
    except Exception:
        return {'Error': 'something went wrong'}


def delete_location(request):
    location_id = request.data.get('id')
    
    try:
        location = Location.objects.get(auto_increment_id=location_id)
        location.delete()
        return True
    except Exception:
        return False
    

def get_all_locations(request):
    
    locations = Location.objects.all()
    serialized = LocationSerializer(locations, many=True)
    return serialized


def get_location_by_id(request):
    location_id = request.data.get('id')
    
    try:
        location = Location.objects.get(auto_increment_id=location_id)
        return LocationSerializer(location)
    except Exception:
        return {'Error': f'The location with the following id {location_id} does not exist!'}
    

def edit_location(request):
    number = request.data.get('number')
    country = request.data.get('country')
    city = request.data.get('city')
    image_url = request.data.get('image_url')
    loc_id = request.data.get('id_loc')
    
    try:
        obj = Location.objects.get(auto_increment_id=loc_id)
        if number:
            obj.number = number
        if country:
            obj.country = country
        if city:
            obj.city = city
        if image_url:
            obj.image_url = image_url
        return LocationSerializer(obj)
    except Exception:
        return False

# HOLIDAY
def create_holiday(data):
    try:
        location_id = data.get('location')
        location_obj = Location.objects.get(id=location_id)

        holiday = Holiday(
            location=location_obj,
            title=data.get('title'),
            start_date=data.get('start_date', datetime.now().date()),
            duration=data.get('duration'),
            price=data.get('price'),
            free_slots=data.get('free_slots'),
        )

        holiday.save()
        return {'Success': 'Holiday was created!'}
    except Location.DoesNotExist:
        return {'Error': 'Location not found with thsi id.'}
    except Exception as e:
        return {'Error': f'Something went wrong while creating the holiday: {str(e)}'}

def delete_holiday(holiday_id):
    try:
        holiday = Holiday.objects.get(id=holiday_id)
        holiday.delete()
        return {'Success': 'Holiday deleted successfully.'}
    except Holiday.DoesNotExist:
        return {'Error': 'Holiday not found with this id.'}
    except Exception as e:
        return {'Error': f'Something went wrong while deleting the holiday: {str(e)}'}

def get_all_holidays():
    holidays = Holiday.objects.all()
    serialized = HolidaySerializer(holidays, many=True)
    return serialized.data

def get_holiday_by_id(holiday_id):
    try:
        holiday = Holiday.objects.get(id=holiday_id)
        serialized = HolidaySerializer(holiday)
        return serialized.data
    except Holiday.DoesNotExist:
        return {'Error': f'The holiday with the following id {holiday_id} does not exist!'}

def edit_holiday(holiday_id, data):
    try:
        holiday = Holiday.objects.get(id=holiday_id)

        location_id = data.get('location')
        if location_id:
            try:
                new_location = Location.objects.get(id=location_id)
                holiday.location = new_location
            except Location.DoesNotExist:
                return {'Error': 'There is no location with this id!'}

        for field in ['title', 'start_date', 'duration', 'price', 'free_slots']:
            if data.get(field) is not None:
                setattr(holiday, field, data[field])
        holiday.save()
        serialized = HolidaySerializer(holiday)
        return serialized.data
    except Holiday.DoesNotExist:
        return {'Error': 'Holiday not found with this id.'}
    ## reservation
def create_reservation(request):
    contact_name = request.data.get('contact_name')
    phone_number = request.data.get('phone_number')
    holiday_id = request.data.get('holiday_id')
    location_id = request.data.get('location_id')
    
    try:
        holiday_obj = Holiday.objects.get(auto_increment_id=holiday_id)
        location_obj = Location.objects.get(auto_increment_id=location_id)
        reservation = Reservation(
            contact_name=contact_name,
            phone_number=phone_number,
            holiday=holiday_obj,
            location=location_obj
        )
        reservation.save()
        return {'Success': 'reservation created '}
    except Exception:
        return {'Error': 'Something went wrong'}
    
    
def delete_reservation(request):
    reserve_id = request.data.get('reservation_id')
    try:
        reseve_obj = Reservation.objects.get(auto_increment_id=reserve_id)
        reseve_obj.delete()
        return {'Success': 'deleted'}
    except Exception:
        return {'Error': 'Could not find reservation with that id!'}
    
    
def get_all_reservations(request):
    reservations = Reservation.objects.all()
    serialized = ReservationSerializer(reservations, many=True)
    return serialized


def get_reservation_by_id(request):
    reserve_id = request.data.get('reservation_id')
    try:
        reserve_obj = Reservation.objects.get(auto_increment_id=reserve_id)
        serialized = ReservationSerializer(reserve_obj)
        return serialized
    except Exception:
        return {'Error': 'There is no existing reservation with this id!'}


def edit_reservation(request):
    reserve_id = request.data.get('reservation_id')
    contact_name = request.data.get('contact_name')
    phone_number = request.data.get('phone_number')
    holiday_id = request.data.get('holiday_id')
    location_id = request.data.get('location_id')
    
    try:
        obj = Reservation.objects.get(auto_increment_id=reserve_id)
        if contact_name:
            obj.contact_name = contact_name
        if phone_number:
            obj.phone_number = phone_number
        if holiday_id:
            try:
                holiday_obj = Holiday.objects.get(auto_increment_id=holiday_id)
            except Exception:
                return {'Error': 'There is no holiday with this id!'}
            obj.holiday = holiday_obj
        if location_id:
            try:
                location_obj = Location.objects.get(auto_increment_id=location_id)
            except Exception:
                return {'Error': 'There is no locaiton with this id!'}
            obj.location=location_obj
        obj.save()
        return ReservationSerializer(obj)
    except Exception:
        return False
        