from django.db import models

class Review(models.Model):
    car = models.ForeignKey('cars.Car', on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=100, null=True, blank=True)
    rating = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField(default='', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} — {self.rating}★"
