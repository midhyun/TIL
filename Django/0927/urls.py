from django.urls import path
from . import views

urlpatterns = [
    path("calculate/<int:num1>/<int:num2>", views.calculate),
    path("oddeven/<int:number>", views.oddeven),
    path("dormitory/", views.dormitory),
    path("dormitory_s/", views.dormitory_s),
    path("lorem_kor/", views.lorem_kor),
    path("lorem_result/", views.lorem_kor_result),
]
