from django.urls import path
from . import api_views as views
urlpatterns = [
    path("", views.QuizListView.as_view()),
    path("<pk>/questions", views.QuizQuestionListView.as_view())
]
