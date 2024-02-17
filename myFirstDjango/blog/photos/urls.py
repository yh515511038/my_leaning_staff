from django.urls import path
from .views import PhotosView, BanBanView

urlpatterns = [
    path("", PhotosView.as_view(), name="photos"),
    path("banban/<int:pk>", BanBanView.as_view(), name="banban"),
]
