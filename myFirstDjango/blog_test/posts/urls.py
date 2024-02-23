from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("posts", views.posts, name="posts"),
    path("post/<int:pk>", views.post, name="post_detail"),
]
