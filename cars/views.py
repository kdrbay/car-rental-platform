from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Car, Category, Rental
from .forms import CarForm

def car_list(request):
    cars = Car.objects.all().order_by('-created_at')
    return render(request, 'cars/car_list.html', {'cars': cars})

@login_required
def car_create(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            car = form.save(commit=False)
            car.owner = request.user
            car.save()
            return redirect('car_list')
    else:
        form = CarForm()
    return render(request, 'cars/car_form.html', {'form': form})

from django.shortcuts import get_object_or_404

@login_required
def rent_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        form = RentalForm(request.POST)
        if form.is_valid():
            rental = form.save(commit=False)
            rental.renter = request.user
            rental.car = car
            rental.save()
            return redirect('car_list')
    else:
        form = RentalForm()
    return render(request, 'cars/rent_car.html', {'form': form, 'car': car})

@login_required
def my_rentals(request):
    rentals = Rental.objects.filter(renter=request.user).order_by('-start_date')
    return render(request, 'cars/my_rentals.html', {'rentals': rentals})

from .forms import ReviewForm

def car_detail(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    reviews = car.reviews.select_related('user').order_by('-created_at')
    review_form = None

    if request.user.is_authenticated:
        if request.method == 'POST':
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                new_review = review_form.save(commit=False)
                new_review.car = car
                new_review.user = request.user
                new_review.save()
                return redirect('car_detail', car_id=car.id)
        else:
            # Если пользователь уже оставлял отзыв — не показываем форму
            if not car.reviews.filter(user=request.user).exists():
                review_form = ReviewForm()

    return render(request, 'cars/car_detail.html', {
        'car': car,
        'reviews': reviews,
        'review_form': review_form
    })

from django.db.models import Q

def car_list(request):
    cars = Car.objects.all()
    categories = Category.objects.all()

    # Фильтрация
    query = request.GET.get('q')
    if query:
        cars = cars.filter(Q(title__icontains=query) | Q(description__icontains=query))

    category_id = request.GET.get('category')
    if category_id:
        cars = cars.filter(category_id=category_id)

    min_price = request.GET.get('min_price')
    if min_price:
        cars = cars.filter(price_per_day__gte=min_price)

    max_price = request.GET.get('max_price')
    if max_price:
        cars = cars.filter(price_per_day__lte=max_price)

    return render(request, 'cars/car_list.html', {
        'cars': cars,
        'categories': categories,
    })

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CarForm
from .models import Car

@login_required
def car_create(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            car = form.save(commit=False)
            car.owner = request.user
            car.save()
            return redirect('car_list')
    else:
        form = CarForm()
    return render(request, 'cars/car_form.html', {'form': form})

@login_required
def car_update(request, pk):
    car = get_object_or_404(Car, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect('car_list')
    else:
        form = CarForm(instance=car)
    return render(request, 'cars/car_form.html', {'form': form})

@login_required
def car_delete(request, pk):
    car = get_object_or_404(Car, pk=pk, owner=request.user)
    if request.method == 'POST':
        car.delete()
        return redirect('car_list')
    return render(request, 'cars/car_confirm_delete.html', {'car': car})

@login_required
def my_cars(request):
    cars = Car.objects.filter(owner=request.user)
    return render(request, 'cars/my_cars.html', {'cars': cars})
