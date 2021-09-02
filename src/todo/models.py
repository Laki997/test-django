from django.db import models
from django.db.models.enums import IntegerChoices
from src.users.models import User
from .constants import PRIORITY_CHOICES


    


class ToDo(models.Model):
    title = models.CharField(max_length = 255)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    class ToDoPriority(IntegerChoices):
         LOW = PRIORITY_CHOICES.get('LOW')
         MEDIUM = PRIORITY_CHOICES.GET('MEDIUM')
         MEDIUM_HIGH = PRIORITY_CHOICES.get('MEDIUM_HIGH')
         HIGH = PRIORITY_CHOICES.get('HIGH')
    priority = models.IntegerField(choices = ToDoPriority.choices, default = ToDoPriority.LOW)