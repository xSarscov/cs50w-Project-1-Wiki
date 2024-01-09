from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:TITLE>", views.entries, name="entries"),
    path("search", views.search, name="search"),
    path("new_page", views.new_page, name="new_page"),
    path("edit_page/<str:TITLE>", views.edit_page, name="edit_page"),
    path("random_page", views.random_page, name="random_page"),
]
