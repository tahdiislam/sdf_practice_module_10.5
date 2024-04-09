from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("page_1/", views.page_1),
    path("page_2/", views.page_2),
]