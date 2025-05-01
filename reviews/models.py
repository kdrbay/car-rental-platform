from django.db import models
from users.models import CustomUser
from cars.models import Car

class Review(models.Model):
    car = models.ForeignKey(Car, related_name='reviews', on_delete=models.CASCADE)
    reviewer = models.ForeignKey(CustomUser, related_name='reviews', on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # Рейтинг от 1 до 5
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review for {self.car} by {self.reviewer}'
