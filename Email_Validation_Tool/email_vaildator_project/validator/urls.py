from django.urls import path
from .views import EmailValidationView

urlpatterns = [
    path("validate-emails/", EmailValidationView.as_view(), name="validate-emails"),
]
