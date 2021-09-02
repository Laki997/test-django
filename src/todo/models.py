from django.db import models
from django.db.models.enums import IntegerChoices
from src.users.models import User


class ToDoPriority(IntegerChoices):
    LOW = 1, 'LOW'
    MEDIUM = 2, 'MEDIUM',
    MEDIUM_HIGH = 3, 'MEDIUM_HIGH',
    HIGH = 4, 'HIGH'


class ToDo(models.Model):
    title = models.CharField(max_length = 255)
    priority = models.IntegerField(choices = ToDoPriority.choices, default = ToDoPriority.LOW)
    user = models.ForeignKey(User, on_delete = models.CASCADE)