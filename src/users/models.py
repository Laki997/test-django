from django.core.checks.messages import Error
from django.db import models
from django.contrib.auth.models import  AbstractUser
from django.db.models.expressions import Value
import uuid


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = None
    email = models.EmailField(('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
