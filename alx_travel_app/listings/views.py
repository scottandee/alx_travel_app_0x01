from rest_framework import viewsets
from .serializers import UserSerializer, BookingSerializer, ListingSerializer
from .models import User, Booking, Listing, Review


class UserViewSets(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class ListingViewSets(viewsets.ModelViewSet):
    serializer_class = ListingSerializer
    queryset = Listing.objects.all()


class BookingViewSets(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()


class ReviewViewSets(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = Review.objects.all()
