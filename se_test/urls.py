from django.contrib import admin
from django.urls import path
from main.views import home_view, login_view, signup_view, landing_view, upload_view, profile_view, show_video_view, video_detail, videos_view
from django.contrib.auth.decorators import login_required
from main.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view, name="home"),
    path("landing/", landing_view, name="landing"),
    path("login/", login_view, name="login"),
    path("signup/", signup_view, name="signup"),
    path("upload_video/", upload_view, name="upload"),
    path("profile/", profile_view, name="profile"),
    path("video/<int:video_id>/", show_video_view, name="show_video"),

    path("videos/<int:video_id>/", video_detail, name="video-detail"),
    path("videos/", videos_view, name="videos")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)