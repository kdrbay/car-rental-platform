from django.contrib import admin
from .models import Car

class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'price_per_day', 'location', 'owner')
    search_fields = ('brand', 'model', 'owner__username')
    list_filter = ('brand', 'location')

admin.site.register(Car, CarAdmin)
