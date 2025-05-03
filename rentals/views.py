from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Rental
from cars.models import Car
from .forms import RentalForm

@login_required
def rent_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)

    if request.method == 'POST':
        form = RentalForm(request.POST)
        if form.is_valid():
            rental = form.save(commit=False)
            rental.car = car
            rental.renter = request.user
            rental.total_cost = car.price_per_day * ((rental.end_date - rental.start_date).days + 1)
            rental.save()
            return redirect('my_rentals')
    else:
        form = RentalForm()

    return render(request, 'rentals/rent_car.html', {'car': car, 'form': form})
