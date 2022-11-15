from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('create/', views.signup, name='signup'),
    path('<int:pk>/detail', views.detail, name='detail'),
    path('<int:pk>/update', views.update, name='update'),
    path('<int:pk>/delete', views.delete, name='delete'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]