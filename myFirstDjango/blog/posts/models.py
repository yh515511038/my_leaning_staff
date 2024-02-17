from django.db import models
from django.core.validators import MinLengthValidator
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from imagekit.models import ProcessedImageField
from imagekit.processors import Adjust, SmartResize, ResizeToFit
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Tag(models.Model):
    caption = models.CharField(max_length=20)
    image = ProcessedImageField(
        upload_to="posts",
        processors=[
            Adjust(contrast=1.2, sharpness=1.1),
            SmartResize(width=50, height=50)
        ],
        format='JPEG',
        options={'quality': 60},
        null=True,
    )

    def __str__(self):
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200, null=True)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True, related_name="posts")
    posted = models.DateField(auto_now=True)        # Only updated after calling save() method if data already exist!
    # content = models.TextField(validators=[MinLengthValidator(10)])
    content = RichTextUploadingField()
    slug = models.SlugField(default="", blank=True, unique=True, db_index=True)
    image = ProcessedImageField(
        upload_to="posts",
        processors=[
            Adjust(contrast=1.2, sharpness=1.1),
            # SmartResize(width=121.34, height=121.34)
            ResizeToFit(121, 121)
        ],
        format='JPEG',
        options={'quality': 60},
        null=True,
    )
    tags = models.ManyToManyField('Tag', null=True, related_name="posts")

    def __str__(self):
        return f"{self.title} - {self.author}"

    def save(self, *kwargs, **args):
        self.slug = slugify(self.title)
        super().save(*kwargs, **args)

class Comment(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField(max_length=300)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
