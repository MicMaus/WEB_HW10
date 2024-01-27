from django.urls import path
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    PasswordResetView,
)
from . import views
from django.urls import reverse_lazy

app_name = "polls"

urlpatterns = [
    path("", views.quotes, name="quotes"),
    path("author/<int:author_id>/", views.author_detail, name="author_detail"),
    path("filtered_quotes/<str:tag>/", views.quotes_by_tag, name="filtered_quotes"),
    path("register/", views.register, name="register"),
    path(
        "login/",
        views.custom_login,
        name="login",
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
    # password reset urls:
    path(
        "password_reset/",
        PasswordResetView.as_view(
            success_url=reverse_lazy("polls:password_reset_done")
        ),
        name="password_reset",
    ),
    path(
        "password_reset_confirm/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            success_url=reverse_lazy("polls:password_reset_complete")
        ),
        name="password_reset_confirm",
    ),
    path(
        "password_reset_done/",
        PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "password_reset_complete/",
        PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
]
