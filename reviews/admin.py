from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('car', 'reviewer', 'rating', 'created_at')
    list_filter = ('rating',)

admin.site.register(Review, ReviewAdmin)
