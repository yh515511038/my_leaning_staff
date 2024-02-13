from django.contrib import admin
from posts.models import Author, Post, Tag, Comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
  list_filter = ("author", "tags", "posted")
  list_display = ("title", "posted", "author")
  prepopulated_fields = {"slug": ("title",)}


class CommentAdmin(admin.ModelAdmin):
  list_display = ["username", "post"]


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
