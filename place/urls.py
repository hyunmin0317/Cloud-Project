from django.urls import path
from place import views

app_name = 'place'

urlpatterns = [
    path('<str:region>/', views.detail, name='detail'),
    path('<str:region>/new_comment/', views.new_comment, name='comment'),
]
