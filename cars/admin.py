from django.contrib import admin
from .models import Car, Category
from .models import Rental

class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'price_per_day', 'location', 'owner')
    search_fields = ('brand', 'model', 'owner__username')
    list_filter = ('brand', 'location')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(Car, CarAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Rental)