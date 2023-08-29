from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import BaseModel


class User(AbstractUser, BaseModel):
    class RoleChoice(models.TextChoices):
        ADMIN = "admin", "Administrator"
        TEACHER = "teacher", "Guru"
        STUDENT = "student", "Pelajar"
    role = models.CharField(max_length=10, choices=RoleChoice.choices, default=RoleChoice.STUDENT)


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
