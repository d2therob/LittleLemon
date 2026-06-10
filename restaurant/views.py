from django.shortcuts import render
from rest_framework import generics
from .models import Booking
from LittleLemonAPI.models import MenuItem
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated



# Create your views here.
def index(request):
    return render(request, 'index.html',{})

class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuSerializer


class SingleMenuItemView(
    generics.RetrieveUpdateAPIView,
    generics.DestroyAPIView
):
    queryset = MenuItem.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(
    viewsets.ModelViewSet
):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
