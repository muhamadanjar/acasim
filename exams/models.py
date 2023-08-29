from django.db import models
from core.models import BaseModel


class Quiz(BaseModel):
    title = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)


class Question(BaseModel):
    content = models.CharField(max_length=200)
    level = models.CharField(max_length=10)
    quiz = models.ManyToManyField(Quiz)

