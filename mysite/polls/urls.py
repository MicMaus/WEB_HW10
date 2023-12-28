from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = "polls"

urlpatterns = [
    path("", views.quotes, name="quotes"),
    path("author/<int:author_id>/", views.author_detail, name="author_detail"),
    path("register/", views.register, name="register"),
    path(
        "login/",
        LoginView.as_view(),
        name="login",
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
]
