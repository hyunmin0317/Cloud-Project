from django.urls import path
from hip import views

app_name = 'hip'

urlpatterns = [
    path('', views.all, name='all'),
    path('index/', views.index, name='index'),
    path('<str:region>/', views.detail, name='detail'),
]
