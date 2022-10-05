from django.urls import path
from . import views

app_name = 'crud'

urlpatterns = [
    path('', views.index , name='index'),
    path('create/', views.create, name='create'),
    path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('detail/<int:pk>', views.detail, name='detail'),
]