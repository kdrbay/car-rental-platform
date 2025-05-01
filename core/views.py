from django.shortcuts import render, get_object_or_404
from cars.models import Car, Category

def home(request):
    cars = Car.objects.all()
    return render(request, 'core/home.html', {'cars': cars})

def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    return render(request, 'core/car_detail.html', {'car': car})

def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    cars = category.cars.all()
    return render(request, 'core/category_detail.html', {'category': category, 'cars': cars})
