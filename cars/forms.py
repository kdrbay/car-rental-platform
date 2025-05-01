from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['brand','model','year','price_per_day','location','description','image','category']

from .models import Rental

class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['start_date', 'end_date']

from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            'comment': forms.Textarea(attrs={'rows': 3}),
        }
