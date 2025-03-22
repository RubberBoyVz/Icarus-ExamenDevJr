from django.urls import path
from . import views

urlpatterns = [
    path('tareas/', views.tarea_list, name='tarea-list'),
    path('tareas/<int:pk>/', views.tarea_detail, name='tarea-detail'),
]