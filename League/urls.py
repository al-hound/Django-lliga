from django.urls import path

from . import views

urlpatterns = [
    path("menu", views.menu, name="menu"),
    path("classificacio/<int:lliga_id>", views.classificacio, name="classificacio"),
    path("taula", views.taula, name="taula"),
]