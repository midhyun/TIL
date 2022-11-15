from django.urls import path
from . import views
app_name = 'todos'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('delete/<int:todo_pk>', views.delete, name='delete'),
    path('edit/<int:todo_pk>', views.edit, name='edit'),
    path('modify/<int:todo_pk>', views.modify, name='modify'),
    path('complete/<int:todo_pk>', views.complete, name='complete'),
]