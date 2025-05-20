from django.shortcuts import render, get_object_or_404, redirect
from cars.models import Car, Category, Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required

def home(request):
    cars = Car.objects.all()
    return render(request, 'core/home.html', {'cars': cars})

def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    reviews = Review.objects.filter(car=car).order_by('-created_at')
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.car = car
            review.user = request.user
            review.save()
            return redirect('car_detail', car_id=car.id)
    else:
        form = ReviewForm()

    return render(request, 'core/car_detail.html', {
    'car': car,
    'reviews': reviews,
    'review_form': form,
})

def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    cars = category.cars.all()
    return render(request, 'core/category_detail.html', {'category': category, 'cars': cars})

from django.shortcuts import render

def car_list(request):
    return render(request, 'core/base.html') 

@login_required
def leave_review(request, car_id):
    car = get_object_or_404(Car, pk=car_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user  # важно: текущий авторизованный пользователь
            review.car = car            # важно: объект Car, а не просто ID
            review.save()
            return redirect('car_detail', car_id=car.id)
    else:
        form = ReviewForm()

    return render(request, 'core/leave_review.html', {
        'form': form,
        'car': car
    })