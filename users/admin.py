from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_number', 'is_seller', 'is_staff')
    search_fields = ('username', 'email')
    list_filter = ('is_seller',)

admin.site.register(CustomUser, CustomUserAdmin)
