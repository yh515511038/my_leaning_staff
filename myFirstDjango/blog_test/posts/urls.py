from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("posts", views.AllPostsView.as_view(), name="posts"),
    path("post/<slug:slug>", views.PostDetailView.as_view(), name="post_detail"),
]
