from django.db import models
from core.models import BaseModel


class Student(BaseModel):
    class GenderChoice(models.TextChoices):
        MALE = "male", "Laki - Laki"
        FEMALE = "female", "Perempuan"
    name = models.CharField(max_length=100)
    address = models.TextField()
    gender = models.CharField(choices=GenderChoice.choices, default=GenderChoice.MALE)

    def __str__(self):
        return f"{self.name} - {self.get_gender_display()}"

    class Meta:
        verbose_name = "Siswa"
        verbose_name_plural = "Siswa - Siswi"
