from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.detail, name='detail'),
    path('<int:article_pk>/update/<int:pk>', views.update, name='update'),
    path('<int:article_pk>/delete/<int:pk>', views.delete, name='delete'),
    path('<int:pk>/comment', views.comment, name='comment'),
    path('<int:article_pk>/comment_delete/<int:pk>', views.comment_delete, name='comment_delete'),
]