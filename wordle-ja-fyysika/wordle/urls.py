from django.urls import path
from . import views

urlpatterns = [
    path("", views.algus, name="algus"),
    path("kontroll/", views.kontroll, name="kontroll"),
]