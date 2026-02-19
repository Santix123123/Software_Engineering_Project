from django.contrib import admin
from django.urls import path
from main.views import home_view, login_view, signup_view, landing_view, upload_view, profile_view
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view, name="home"),
    path("landing/", landing_view, name="landing"),
    path("login/", login_view, name="login"),
    path("signup/", signup_view, name="signup"),
    path("upload_video/", upload_view, name="upload"),
    path("profile/", profile_view, name="profile")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
                          document_root=settings.MEDIA_ROOT)