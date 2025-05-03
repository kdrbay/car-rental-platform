from django.contrib import admin
from .models import Car, Category
from .models import Rental, Review

class CarAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not change:  # если создается новая машина
            obj.owner = request.user
        super().save_model(request, obj, form, change)
        
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(Car, CarAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Rental)
admin.site.register(Review)