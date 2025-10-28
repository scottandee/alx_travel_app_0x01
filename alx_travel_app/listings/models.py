import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator


class UserRole(models.TextChoices):
    GUEST = 'guest'
    HOST = 'host'
    ADMIN = 'admin'


class User(AbstractUser):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, db_index=True)
    password_hash = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    role = models.CharField(max_length=20, choices=UserRole.choices)
    created_at = models.DateTimeField(auto_now_add=True)

    
class Listing(models.Model):
    property_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    host_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class BookingStatus(models.TextChoices):
    PENDING = 'pending'
    CONFIRMED = 'confirmed'
    CANCELLED = 'cancelled'


class Booking(models.Model):
    booking_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bookings")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=BookingStatus.choices)
    created_at = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    review_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="listings")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
