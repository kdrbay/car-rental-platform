from django.db import models
from users.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='cars/', blank=True, null=True)
    category = models.ForeignKey(Category, related_name='cars', on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey(User, related_name='cars', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.brand} {self.model} ({self.year})'

from django.utils import timezone

class Rental(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='car_rentals')
    renter = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.renter.username} → {self.car.title}"

    def is_active(self):
        return self.end_date >= timezone.now().date()
