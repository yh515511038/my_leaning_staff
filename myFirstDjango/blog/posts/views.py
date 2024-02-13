from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from posts.models import Post, Comment
from posts.forms import CommentForm

# Create your views here.
class IndexView(ListView):
  template_name = 'posts/index.html'
  model = Post
  ordering = ["-posted"]
  context_object_name = "posts"

  def get_queryset(self):
    queryset = super().get_queryset()
    return queryset[:3]   # Get 3 latest posts


class PostsView(ListView):
  template_name = 'posts/posts.html'
  model = Post
  ordering = ["-posted"]
  context_object_name = "posts"


class PostDetailView(View):
  def get(self, request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, "posts/post_detail.html", {
      "post": post,
      "tags": post.tags.all(),
      "comments": post.comments.all().order_by("-id"),
      "comment_form": CommentForm()
    })

  def post(self, request, slug):    # slug is already a part of URL from urls.py
    comment_form = CommentForm(request.POST)
    post = Post.objects.get(slug=slug)

    if comment_form.is_valid():
      # Add 'post' column of 'Comment' Model 
      new_comment = comment_form.save(commit=False)   # Not commit to DB but create one Record instance
      new_comment.post = post
      new_comment.save()
      return HttpResponseRedirect(reverse('post-detail', args=[slug]))

    return render(request, "posts/post_detail.html", {
      "post": post,
      "tags": post.tags.all(),
      "comments": post.comments.all().order_by("-id"),
      "comment_form": comment_form
    })

# class CommentView(CreateView):
#   template_name = "posts/comment.html"
#   model = Comment
#   fields = "__all__"
#   success_url = "/posts/"

#   def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#     print(f'self.object: {self.object}')
#     context["post"] = self.object
#     return context

# def comments(request, slug):
#   post = get_object_or_404(Post, slug=slug)
#   form = CommentForm()
#   return render(request, 'posts/comments.html', {
#     "post": post,
#     "form": form,
#   })


class ReadLaterView(View):
  def get(self, request):
    stored_posts = request.session.get("stored_posts")

    read_later_posts = []
    if stored_posts:
      read_later_posts = Post.objects.filter(id__in=stored_posts)

    return render(request, "posts/stored_posts.html", {
      "read_later_posts": read_later_posts
    })
  
  def post(self, request):
    stored_posts = request.session.get("stored_posts")

    if stored_posts is None:
      stored_posts = []
    
    post_id = int(request.POST.get("post_id"))

    if post_id not in stored_posts:
      stored_posts.append(post_id)
      request.session["stored_posts"] = stored_posts
    
    return HttpResponseRedirect("/")
