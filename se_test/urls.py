from django.contrib import admin
from django.urls import path
from main.views import login_view, signup_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", signup_view, name="home"),
    path("login/", login_view, name="login"),
    path("signup/", signup_view, name="signup"),
]