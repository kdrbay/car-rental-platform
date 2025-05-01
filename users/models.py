from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    is_seller = models.BooleanField(default=False)  # Роль продавца

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',  # Добавляем related_name
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='user'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',  # Добавляем related_name
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='user'
    )

    def __str__(self):
        return self.username
