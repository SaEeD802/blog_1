from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('<int:pk>/', views.detail, name='detail'),
    path('add/', views.create, name='add'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]
