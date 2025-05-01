from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
]
