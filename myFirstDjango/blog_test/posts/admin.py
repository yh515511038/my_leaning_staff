from django.contrib import admin
from .models import Post, Author, Comment

# Register your models here.
class PostAdmin(admin.ModelAdmin):
  list_display = ["title", "author"]
  list_filter = ["author"]
  prepopulated_fields = {"slug": ("title", )}

class AuthorAdmin(admin.ModelAdmin):
  list_display = ["name", "email"]

admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Comment)
