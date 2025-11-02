from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializers import UserSerializer, BookingSerializer, ListingSerializer
from .models import User, Booking, Listing, Review


class ListingViewSets(viewsets.ModelViewSet):
    serializer_class = ListingSerializer
    queryset = Listing.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookingViewSets(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    permission_classes = [IsAuthenticated]


class ReviewViewSets(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = Review.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

