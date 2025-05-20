from .forms import ReviewForm

def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    reviews = car.reviews.order_by('-created_at')

    if request.method == 'POST' and 'submit_review' in request.POST:
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.car = car
            review.save()
            return redirect('car_detail', pk=car.pk)
    else:
        review_form = ReviewForm()

    return render(request, 'car_detail.html', {
        'car': car,
        'reviews': reviews,
        'review_form': review_form,
    })
