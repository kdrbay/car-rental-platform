from django.urls import path
from . import views

urlpatterns = [
    path('car/<int:car_id>/review/', views.leave_review, name='leave_review'),
]