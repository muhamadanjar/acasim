from django.urls import path
from . import api_views as views

urlpatterns = [
    path("", views.UserListView.as_view()),
    path("<pk>/detail", views.UserDetailView.as_view()),
]