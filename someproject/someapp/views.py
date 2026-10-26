from rest_framework import viewsets
from .models import Tour, Booking
from .serializers import TourSerializer, BookingSerializer

class TourViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer