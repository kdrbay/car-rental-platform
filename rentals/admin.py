from django.contrib import admin
from .models import Rental

class RentalAdmin(admin.ModelAdmin):
    list_display = ('car', 'renter', 'start_date', 'end_date', 'total_cost', 'status')
    list_filter = ('status',)

admin.site.register(Rental, RentalAdmin)
