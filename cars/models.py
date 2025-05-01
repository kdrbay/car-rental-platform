from django.db import models

class Car(models.Model):
    owner = models.ForeignKey('users.User', related_name='cars', on_delete=models.CASCADE)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='car_images/', null=True, blank=True)

    def __str__(self):
        return f'{self.brand} {self.model} ({self.year})'
