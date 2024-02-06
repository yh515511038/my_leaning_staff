from django.contrib import admin
from posts.models import Author, Post

# Register your models here.
admin.site.register(Post)
admin.site.register(Author)
