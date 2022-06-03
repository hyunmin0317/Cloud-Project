from django.urls import path
from place import views

app_name = 'place'

urlpatterns = [
    path('<str:region>/', views.detail, name='detail'),
    path('<str:region>/new_comment/', views.new_comment, name='comment'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='comment_delete'),
    path('comment/modify/<int:comment_id>/', views.modify_comment, name='modify_comment'),
]
