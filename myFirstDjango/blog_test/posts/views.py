from django.shortcuts import render
from .forms import CommentForm
from .models import Post, Comment

# Create your views here.
def index(request):
  posts = Post.objects.order_by("-posted")[:4]
  return render(request, "posts/index.html", {
    "posts": posts
  })


def posts(request):
  posts = Post.objects.all()
  return render(request, "posts/posts.html", {
    "posts": posts,
  })


def post(request, id):
  if request.method == 'POST':
    comment_username = request.POST["username"]
    comment_content = request.POST["content"]
    post = Post.objects.get(id=id)
    new_comment = Comment(username=comment_username, content=comment_content, post=post)
    new_comment.save()
  post = Post.objects.get(id=id)
  form = CommentForm()
  return render(request, "posts/post.html", {
    "post": post,
    "form": form
  })
