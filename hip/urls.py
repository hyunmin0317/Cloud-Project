from django.urls import path
from hip import views

app_name = 'hip'

urlpatterns = [
    path('<str:region>/', views.detail, name='detail'),
    path('profile/<str:name>/', views.myprofile, name='profile'),
    path('profile/<str:name>/update/', views.update, name='update'),
]
