from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.detail, name='detail'),
    path('<int:pk>/update', views.update, name='update'),
    path('<int:pk>/delete', views.delete, name='delete'),
    path('<int:article_pk>/comments', views.comments, name='comments'),
    path('<int:article_pk>/delete_comments/<int:pk>', views.delete_comments, name='delete_comments'),
]