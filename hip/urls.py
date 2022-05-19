from django.urls import path, include
from hip import views

urlpatterns = [
    path('', views.home),
    path('<str:region>/', views.hip),
]
