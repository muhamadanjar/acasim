from django.urls import path, include
from . import views

urlpatterns = [
    path("accounts/", include("accounts.api_urls")),
	path("login",views.LoginApiView.as_view()),
]
