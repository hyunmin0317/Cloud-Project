from django.urls import path, include
from hip import views

urlpatterns = [
    path('', views.all),
    path('<str:region>/', views.detail),
]
