from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_list, name='car_list'),
    path('new/', views.car_create, name='car_create'),
    path('rent/<int:car_id>/', views.rent_car, name='rent_car'),
    path('my-rentals/', views.my_rentals, name='my_rentals'),
    path('cars/', views.car_list, name='car_list'),
    path('create/', views.car_create, name='car_create'),
    path('<int:pk>/edit/', views.car_update, name='car_update'),
    path('<int:pk>/delete/', views.car_delete, name='car_delete'),
]
