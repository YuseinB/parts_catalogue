from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)

    def __str__(self):
        return self.user.username


User._meta.get_field('username').validators.append(MinLengthValidator(limit_value=4))
