from django.urls import path, include
from hip import views

urlpatterns = [
    path('', views.all),
    path('index/', views.index),
    path('<str:region>/', views.detail),
]
