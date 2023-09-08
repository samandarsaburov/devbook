from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    phone = models.CharField(default='', max_length=15)
    CHOISE_ROLES = (
        (3, 'admin'),
        (2, 'writer'),
        (1, 'reader')
    )
    roles = models.PositiveSmallIntegerField(default=1, choices=CHOISE_ROLES)
