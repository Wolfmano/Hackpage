from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Абитуриент'),
        ('mentor', 'Наставник'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='student')

