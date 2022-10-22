from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("<int:pk>/accounts_update/", views.accounts_update, name="accounts_update"),
    path("password_update/", views.password_update, name="password_update"),
    path("<int:pk>/", views.detail, name="detail"),
]
