from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('edit/<int:pk>/', views.edit_post, name='edit'),
    path('delete/<int:pk>/', views.delete_post, name='delete'),
]
