from django.urls import path
from place import views


urlpatterns = [
    path('<str:region>/', views.detail),
]
