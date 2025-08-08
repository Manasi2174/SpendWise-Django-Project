# tracker/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add-income/', views.add_income, name='add_income'),
    path('add-expense/', views.add_expense, name='add_expense'),
    path('edit-income/<int:pk>/', views.edit_income, name='edit_income'),
    path('delete-income/<int:pk>/', views.delete_income, name='delete_income'),
    path('edit-expense/<int:pk>/', views.edit_expense, name='edit_expense'),
    path('delete-expense/<int:pk>/', views.delete_expense, name='delete_expense'),
     path('register/', views.register_view, name='register'),
]
