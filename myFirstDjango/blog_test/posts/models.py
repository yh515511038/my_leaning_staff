from django.db import models

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=50)
  author = models.CharField(max_length=50)
  image = models.ImageField(upload_to='uploads')
  content = models.TextField()
  desc = models.CharField(max_length=100)
  posted = models.DateTimeField(auto_now=True)
  
  def __repr__(self):
    return f"{self.title} - {self.author}"


class Comment(models.Model):
  username = models.CharField(max_length=50)
  content = models.TextField()
  post = models.ForeignKey('Post', on_delete=models.CASCADE, null=True, related_name="comments")
