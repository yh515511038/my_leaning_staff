from typing import Any
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, CreateView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from .forms import CommentForm
from .models import Post, Comment

# Create your views here.
class IndexView(TemplateView):
  template_name = "posts/index.html"
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["posts"] = Post.get_all_by_time()[:4]
    return context


class AllPostsView(ListView):
  template_name = "posts/posts.html"
  model = Post
  context_object_name = "posts"


class PostDetailView(View):
  def get(self, request, slug):
    post = Post.get_by_slug(slug)
    form = CommentForm()
    comments = post.comments.all().order_by("-id")
    return render(request, "posts/post.html", {
      "post": post,
      "form": form,
      "comments": comments,
    })
  
  def post(self, request, slug):
    post = Post.get_by_slug(slug)
    post_form = CommentForm(request.POST)
    comments = post.comments.all().order_by("-id")
    if post_form.is_valid():
      new_comment = post_form.save(commit=False)
      new_comment.post = post
      new_comment.save()
      
      return HttpResponseRedirect(reverse("post_detail", kwargs={"slug": slug}))
    
    return render(request, "posts/post.html", {
      "post": post,
      "form": post_form,
      "comments": comments,
    })
