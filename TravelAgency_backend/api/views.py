from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from django.http import JsonResponse

# Create your views here.

class HolidayView(APIView):
    def get(self, request):
        return handle_response_data(get_all_holidays(request))
    def post(self, request):
        return handle_response(create_holiday(request))
    def put(self, request):
        return handle_response_data(edit_holiday(request))
    def delete(self, request):
        return handle_response(delete_holiday(request))


class HolidaySupportView(APIView):
    def get(self, request):
        return handle_response_data(get_holiday_by_id(request))
    
    
class LocationView(APIView):
    def get(self, request):
        return handle_response_data(get_all_locations(request))
        
    def post(self, request):
        return handle_response(create_location(request))
    
    def put(self, request):
        return handle_response_data(edit_location(request))
    
    def delete(self, request):
        return handle_response(delete_location(request))
    

class LocationSupportView(APIView):
    def get(self, request):
        return handle_response_data(get_location_by_id(request))
    
    
class ReservationView(APIView):    
    def get(self, request):
        return handle_response_data(get_all_reservations(request))
    def post(self, request):
        return handle_response(create_reservation(request))
    def put(self, request):
        return handle_response_data(edit_reservation(request))
    def delete(self, request):
        return handle_response(delete_reservation(request))


class ReservationSupportView(APIView):
    def get(self, request):
        return handle_response_data(get_reservation_by_id(request))
    

# ---- support---- #
def handle_response(msg):
    if isinstance(msg, dict) and 'Error' in msg.keys():
        return JsonResponse(data=msg, status=status.HTTP_400_BAD_REQUEST)
    else:
        return JsonResponse(data=msg, status=status.HTTP_200_OK, safe=False)


def handle_response_data(msg):
    if isinstance(msg, dict) and 'Error' in msg.keys():
        return JsonResponse(data=msg, status=status.HTTP_200_OK, safe=False)
    else:
        return JsonResponse(data=msg.data, status=status.HTTP_200_OK, safe=False)