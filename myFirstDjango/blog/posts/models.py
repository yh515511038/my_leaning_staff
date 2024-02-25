from django.db import models
from django.core.validators import MinLengthValidator
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from imagekit.models import ProcessedImageField
from imagekit.processors import Adjust, SmartResize, ResizeToFit
from ckeditor_uploader.fields import RichTextUploadingField
from django_ckeditor_5.fields import CKEditor5Field


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()
    
    @classmethod
    def get_by_id(self, id):
        return Author.objects.get(id=id)


class Tag(models.Model):
    caption = models.CharField(max_length=20)
    image = ProcessedImageField(
        upload_to="posts",
        processors=[
            Adjust(contrast=1.2, sharpness=1.1),
            SmartResize(width=50, height=50)
        ],
        format='JPEG',
        options={'quality': 80},
        null=True,
    )

    def __str__(self):
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200, null=True)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True, related_name="posts", db_index=True)
    posted = models.DateField(auto_now=True)        # Only updated after calling save() method if data already exist!
    # body = RichTextUploadingField(default="")
    content = CKEditor5Field('Text', config_name='extends', default="")
    slug = models.SlugField(null=False, unique=True, db_index=True)
    image = ProcessedImageField(
        upload_to="posts",
        processors=[
            Adjust(contrast=1.2, sharpness=1.1),
            # SmartResize(width=144, height=1144)
            ResizeToFit(144, 144)
        ],
        format='JPEG',
        options={'quality': 90},
        null=True,
    )
    tags = models.ManyToManyField('Tag', null=True, related_name="posts")

    def __str__(self):
        return f"{self.title} - {self.author}"

    # Slug auto save method(Not for chinese)
    # def save(self, *kwargs, **args):
    #     self.slug = slugify(self.title)
    #     super().save(*kwargs, **args)
        
    @classmethod
    def get_all(self):
        return Post.objects.all()
    
    @classmethod
    def get_by_author(self, author):
        return Post.objects.filter(author=author)

class Comment(models.Model):
    username = models.CharField(max_length=100)
    text = models.TextField(max_length=300)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
