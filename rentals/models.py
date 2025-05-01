from django.db import models
from users.models import CustomUser
from cars.models import Car

class Rental(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='rental_records')
    renter = models.ForeignKey(CustomUser, related_name='rentals', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('completed', 'Completed')], default='pending')

    def __str__(self):
        return f'Rental of {self.car} by {self.renter}'
