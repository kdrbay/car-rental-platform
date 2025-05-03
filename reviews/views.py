from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import ReviewForm
from cars.models import Car

@login_required
def leave_review(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.reviewer = request.user
            review.car = car
            review.save()
            return redirect('car_detail', car_id=car.id)
    else:
        form = ReviewForm()
    return render(request, 'reviews/leave_review.html', {'form': form, 'car': car})
