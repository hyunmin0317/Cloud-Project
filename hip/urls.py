from django.urls import path
from hip import views

app_name = 'hip'

urlpatterns = [
    path('<str:region>/', views.detail, name='detail'),
    path('like/all/', views.all, name='all'),
]
