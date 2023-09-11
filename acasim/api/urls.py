from django.urls import path, include

urlpatterns = [
    path("accounts/", include("accounts.api_urls"))
]
