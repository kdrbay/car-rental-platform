from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15, required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # Импортируй свою модель

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')  # добавь нужные поля

from django import forms
from .models import CustomUser
import re

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'phone_number']

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        if not re.match(r'^\+7\d{10}$', phone):
            raise forms.ValidationError("Номер должен начинаться с +7 и содержать 11 цифр.")
        return phone

from django import forms
from .models import CustomUser
import re
from django.contrib.auth import get_user_model

User = get_user_model()

class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'phone_number']

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        # Удаляем всё, кроме цифр
        digits = re.sub(r'\D', '', phone)

        if not digits.startswith('7') or len(digits) != 11:
            raise forms.ValidationError('Введите корректный в формате +7 (XXX) XXX-XX-XX')

        return f'+7{digits[1:]}'  # сохраняем в формате +7XXXXXXXXXX
