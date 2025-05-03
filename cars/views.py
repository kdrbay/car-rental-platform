from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Car, Category, Rental
from .forms import CarForm, RentalForm, ReviewForm
from django.utils import timezone

# ===== Список автомобилей с фильтрами и пагинацией =====
def car_list(request):
    categories = Category.objects.all()
    cars = Car.objects.all()

    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price:
        cars = cars.filter(price_per_day__gte=min_price)
    if max_price:
        cars = cars.filter(price_per_day__lte=max_price)

    category = request.GET.get('category')
    if category:
        cars = cars.filter(category__name=category)

    query = request.GET.get('q')
    if query:
        cars = cars.filter(Q(title__icontains=query) | Q(description__icontains=query))

    paginator = Paginator(cars, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'cars/car_list.html', {
        'page_obj': page_obj,
        'categories': categories,
    })

# ===== Только админ может добавлять машины =====
@staff_member_required
def car_create(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            car = form.save(commit=False)
            car.owner = request.user
            car.save()
            return redirect('car_detail', pk=car.pk)
    else:
        form = CarForm()
    return render(request, 'cars/car_form.html', {'form': form})

# ===== Только админ может редактировать машины =====
@staff_member_required
def car_update(request, pk):
    car = get_object_or_404(Car, pk=pk)
    form = CarForm(request.POST or None, request.FILES or None, instance=car)
    if form.is_valid():
        form.save()
        return redirect('car_list')
    return render(request, 'cars/car_form.html', {'form': form})

# ===== Только админ может удалять машины =====
@staff_member_required
def car_delete(request, pk):
    car = get_object_or_404(Car, pk=pk)
    car.delete()
    return redirect('car_list')

# ===== Только админ видит список своих машин =====
@staff_member_required
def my_cars(request):
    cars = Car.objects.filter(owner=request.user)
    return render(request, 'cars/my_cars.html', {'cars': cars})

# ===== Страница аренды машины =====
@login_required
def rent_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)

    if car.owner == request.user:
        messages.error(request, "Вы не можете арендовать собственную машину.")
        return redirect('car_list')

    if request.method == 'POST':
        form = RentalForm(request.POST)
        if form.is_valid():
            start = form.cleaned_data['start_date']
            end = form.cleaned_data['end_date']

            overlapping = Rental.objects.filter(
                car=car,
                start_date__lt=end,
                end_date__gt=start
            ).exists()

            if overlapping:
                messages.error(request, "Автомобиль уже арендован на выбранные даты.")
            else:
                rental = form.save(commit=False)
                rental.car = car
                rental.renter = request.user
                rental.save()
                messages.success(request, "Аренда оформлена успешно.")
                return redirect('my_rentals')
    else:
        form = RentalForm()

    return render(request, 'cars/rent_car.html', {'car': car, 'form': form})

# ===== Мои аренды =====
@login_required
def my_rentals(request):
    rentals = Rental.objects.filter(renter=request.user).order_by('-start_date')
    return render(request, 'cars/my_rentals.html', {'rentals': rentals})

# ===== Детали автомобиля и отзывы =====
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
            if not car.reviews.filter(user=request.user).exists():
                review_form = ReviewForm()

    return render(request, 'cars/car_detail.html', {
        'car': car,
        'reviews': reviews,
        'review_form': review_form
    })
