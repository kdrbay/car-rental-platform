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
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'password1': forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Подтвердите пароль'}),
        }
        
    def clean_password1(self):
        password = self.cleaned_data.get("password1")
        # Можно добавить свою логику для проверки пароля (например, длинна и т.д.)
        return password
