from django import forms
from .models import Rental
from django.utils import timezone

class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['start_date', 'end_date']

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get('start_date')
        end = cleaned_data.get('end_date')

        if start and end:
            if start < timezone.now().date():
                raise forms.ValidationError('Дата начала не может быть в прошлом.')
            if end < start:
                raise forms.ValidationError('Дата окончания не может быть раньше начала.')
