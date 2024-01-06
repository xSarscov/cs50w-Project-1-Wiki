from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:TITLE>", views.entries, name="entries"),
    path("search", views.search, name="search"),
]
