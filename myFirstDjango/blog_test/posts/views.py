from django.shortcuts import render
from .forms import CommentForm
from .models import Post, Comment

# Create your views here.
def index(request):
  posts = Post.get_all_by_time()[:4]
  return render(request, "posts/index.html", {
    "posts": posts
  })


def posts(request):
  posts = Post.get_all()
  return render(request, "posts/posts.html", {
    "posts": posts,
  })


def post(request, pk):
  post = Post.get_by_id(pk)

  if request.method == 'POST':
    comment_username = request.POST["username"]
    comment_content = request.POST["content"]
    new_comment = Comment(username=comment_username, content=comment_content, post=post)
    new_comment.save()
  form = CommentForm()
  comments = post.comments.all().order_by("-id")
  return render(request, "posts/post.html", {
    "post": post,
    "form": form,
    "comments": comments,
  })
