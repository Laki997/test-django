from django.db import models
from src.users import models as users_models


# Create your models here.

class ToDo(models.Model):
    title = models.CharField(max_length=255)
    REACT = 'REACT'
    DJANGO = 'DJANGO'
    JAVASCRIPT = 'JAVASCRIPT'
    LARAVEL='LARAVEL'

    PRIORITY_CHOICES = [
         (REACT,'REACT'),
         (DJANGO,'DJANGO'),
         (JAVASCRIPT,'JAVASCRIPT'),
         (LARAVEL,'LARAVEL')
    ]
    priority = models.CharField(
        choices= PRIORITY_CHOICES,
        max_length=15
    )
    user = models.ForeignKey(users_models.User, on_delete=models.CASCADE)