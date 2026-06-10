from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Booking
from LittleLemonAPI.models import MenuItem

class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = MenuItem
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = '__all__'
