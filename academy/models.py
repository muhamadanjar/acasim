from django.db import models

from accounts.models import User
from core.models import BaseModel


class Subject(BaseModel):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)


class Student(BaseModel):
    class GenderChoice(models.TextChoices):
        MALE = "male", "Laki - Laki"
        FEMALE = "female", "Perempuan"
    name = models.CharField(max_length=100)
    address = models.TextField()
    gender = models.CharField(choices=GenderChoice.choices, default=GenderChoice.MALE)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.get_gender_display()}"

    class Meta:
        verbose_name = "Siswa"
        verbose_name_plural = "Siswa - Siswi"


class Teacher(BaseModel):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    joined_date = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)