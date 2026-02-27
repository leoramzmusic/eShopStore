from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('shopkeeper', 'Shopkeeper / POS'),
        ('customer', 'Customer'),
        ('editor', 'CMS Editor'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return self.username
