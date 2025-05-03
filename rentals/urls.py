from django.urls import path
from . import views

urlpatterns = [
    path('car/<int:car_id>/', views.rent_car, name='rent_car'),
]