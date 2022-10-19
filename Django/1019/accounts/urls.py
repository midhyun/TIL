from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns =[
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('<int:pk>', views.detail, name='detail'),
    path('<int:pk>/update', views.update, name='update'),
    path('<int:pk>/delete', views.delete, name='delete'),
    path('error', views.error, name='error'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    ]