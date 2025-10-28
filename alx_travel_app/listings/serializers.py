from rest_framework import serializers
from ....alx_travel_app.alx_travel_app.listings.models import Listing, Booking, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'


class BookingSerializer(serializers.Serializer):
    class Meta:
        model = Booking
        fields = '__all__'