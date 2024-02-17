from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("posts", views.PostsView.as_view(), name="posts"),
    path('post/create', views.AddPost.as_view(), name='add_post'),
    path("post/<slug:slug>", views.PostDetailView.as_view(), name="post-detail"),
    path("read-later", views.ReadLaterView.as_view(), name="read-later"),
    path("tags", views.TagListView.as_view(), name="all-tags"),
    path("tag/<int:tag_id>", views.TaggedPostListView.as_view(), name="tagged_post_list"),
]
