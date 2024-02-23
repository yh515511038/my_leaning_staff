from django.db import models
from django.urls import reverse


# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=50)
  author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True, related_name="posts")
  image = models.ImageField(upload_to='uploads')
  content = models.TextField()
  desc = models.CharField(max_length=100)
  posted = models.DateTimeField(auto_now=True)
  slug = models.SlugField(default="", null=False, db_index=True)
  
  def __str__(self):
    return f"{self.title} - {self.author}"
  
  def get_absolute_url(self):
      return reverse("post_detail", kwargs={"pk": self.pk})
  
  
  @classmethod
  def get_all(self):
    return Post.objects.all()

  @classmethod
  def get_by_id(self, pk):
    return Post.objects.get(pk=pk)
  
  @classmethod
  def get_all_by_time(self):
    return Post.objects.order_by("-posted")


class Comment(models.Model):
  username = models.CharField(max_length=50)
  content = models.TextField()
  post = models.ForeignKey('Post', on_delete=models.CASCADE, null=True, related_name="comments")


class Author(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField(default=None)
  
  def __str__(self):
    return f"{self.name}"
