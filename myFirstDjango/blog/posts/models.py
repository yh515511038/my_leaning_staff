from django.db import models
from django.utils.text import slugify

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, null=True, related_name="posts")
    posted = models.DateField(auto_now=True)        # Only updated after calling save() method if data already exist!
    content = models.TextField()
    slug = models.SlugField(default="", blank=True)
    image = models.CharField(max_length=100, default="mountains.jpg")

    def __str__(self):
        return f"{self.title} - {self.author}"

    def save(self, *kwargs, **args):
        self.slug = slugify(self.title)
        super().save(*kwargs, **args)
