from django.urls import path
from . import views;

urlpatterns = [
    path('', views.index, name="index"),
    path('rooms/', views.index, name="rooms"),
    path('reserves/', views.reserves, name="reserves"),
    path('reserve/', views.reserve, name="reserve"),
    path('show_room/', views.show_room, name="show_room"),
    path('add_reserve/', views.add_reserve, name="add_reserve"),
]