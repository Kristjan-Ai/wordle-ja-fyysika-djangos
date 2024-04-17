from django.urls import path
from . import views

urlpatterns = [
    path('play/', views.sudoku),
    path('create_sudoku/', views.create_sudoku, name='create_sudoku'),
]


