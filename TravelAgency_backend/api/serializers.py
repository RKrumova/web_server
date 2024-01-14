from rest_framework import serializers
from api.models import Holiday, Location, Reservation


class CommonModelSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True
        fields = '__all__'

class HolidaySerializer(CommonModelSerializer):
    class Meta(CommonModelSerializer.Meta):
        model = Holiday

class LocationSerializer(CommonModelSerializer):
    class Meta(CommonModelSerializer.Meta):
        model = Location

class ReservationSerializer(CommonModelSerializer):
    class Meta(CommonModelSerializer.Meta):
        model = Reservation
