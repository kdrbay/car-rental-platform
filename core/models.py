# core/models.py
from django.db import models
from django.contrib.auth import get_user_model
from users.models import CustomUser

User = get_user_model()

class Car(models.Model):
    # твои поля для машины
    title = models.CharField(max_length=100)
    drive_type = models.CharField(max_length=50, blank=True)
acceleration = models.FloatField(null=True, blank=True)
color = models.CharField(max_length=50, blank=True)
interior_color = models.CharField(max_length=50, blank=True)
seats = models.IntegerField(null=True, blank=True)
engine_power = models.IntegerField(null=True, blank=True)
top_speed = models.IntegerField(null=True, blank=True)

    # и т.д.

class Review(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='core_reviews')
    car = models.ForeignKey('cars.Car', on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
