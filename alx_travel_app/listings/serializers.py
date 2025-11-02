from rest_framework import serializers
from .models import Listing, Booking, User, Review


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'user_id',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'role',
            'created_at',
        ]
        read_only_fields = ['user_id', 'created_at', 'role']


class BookingSerializer(serializers.ModelSerializer):
    listing_id = serializers.PrimaryKeyRelatedField(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Booking
        fields = [
            'booking_id',
            'listing_id',
            'user_id',
            'start_date',
            'end_date',
            'total_price',
            'status',
            'created_at'
        ]
        read_only_fields = ['listing_id', 'created_at']


class ListingSerializer(serializers.ModelSerializer):
    host_id = serializers.PrimaryKeyRelatedField(read_only=True)
    bookings = BookingSerializer(many=True, read_only=True)

    class Meta:
        model = Listing
        fields = [
            'listing_id',
            'host_id',
            'name',
            'description',
            'location',
            'price_per_night',
            'created_at',
            'updated_at',
            'bookings',
        ]
        read_only_fields = ['listing_id', 'created_at', 'updated_at']


class ReviewSerializer(serializers.Serializer):
    class Meta:
        model = Review
        fields = [
            'review_id',
            'listing_id',
            'user_id',
            'rating',
            'comment',
            'created_at'
        ]
        read_only_fields = ['review_id', 'created_at']
