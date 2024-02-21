from django.shortcuts import render
from .forms import CommentForm

# Create your views here.
def index(request):
  return render(request, "posts/index.html")


def posts(request):
  return render(request, "posts/posts.html")


def post(request):
  form = CommentForm()
  return render(request, "posts/post.html", {
    "form": form
  })
