from django.contrib import admin
from django.urls import path
from main.views import login_view, signup_view, home_view, landing_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view, name="home"),
    path("landing/", landing_view, name="landing"),
    path("login/", login_view, name="login"),
    path("signup/", signup_view, name="signup"),
]