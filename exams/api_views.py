from oauth2_provider.views import ProtectedResourceView

from .models import Question
from .serializer import QuizSerializer
from rest_framework import generics, permissions


class QuizListView(ProtectedResourceView):
    server_class = QuizSerializer


class QuizQuestionListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Question.objects.all()
    required_scopes = ['student']
