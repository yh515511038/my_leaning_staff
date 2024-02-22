from django.shortcuts import render
from .forms import CommentForm
from .models import Post

# Create your views here.
def index(request):
  posts = Post.objects.order_by("-posted")[:3]
  return render(request, "posts/index.html", {
    "posts": posts
  })


def posts(request):
  return render(request, "posts/posts.html")


def post(request, id):
  post = Post.objects.filter(id=id)[0]
  form = CommentForm()
  return render(request, "posts/post.html", {
    "post": post,
    "form": form
  })
