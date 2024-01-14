from django.urls import path
from api.views import HolidayView, HolidaySupportView, LocationView, LocationSupportView, ReservationSupportView, ReservationView
urlpatterns = [
    path('holidays/', HolidayView.as_view()),
    path('holiday/get_by_id/', HolidaySupportView.as_view()),
    path('locations/', LocationView.as_view()),
    path('location/get_by_id/', LocationSupportView.as_view()),
    path('reservations/', ReservationView.as_view()),
    path('reservation/get_by_id/', ReservationSupportView.as_view()),
]