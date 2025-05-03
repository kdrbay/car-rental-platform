from django.db import models
from users.models import CustomUser

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Car(models.Model):
    title = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='cars/', null=True, blank=True)  # Исправлено: 'modelas' на 'models'
    category = models.ForeignKey(Category, related_name='cars', on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey(CustomUser, related_name='cars', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.brand} {self.model} ({self.year})'

from django.utils import timezone

class Rental(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='car_rentals')
    renter = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def is_active(self):
        return self.end_date >= timezone.now().date()

from django.db import models

class Review(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='car_reviews')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=5)  # от 1 до 5
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('car', 'user')  # Один отзыв на машину от одного пользователя

    def __str__(self):
        return f"Отзыв от {self.user.username} на {self.car.title}"