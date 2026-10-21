from django.urls import path
from . import views

urlpatterns = [
    path("", views.part_list, name="part_list"),
    path("add/", views.add_part, name="add_part"),
    path("hello/", views.hello_world, name="hello_world")
]