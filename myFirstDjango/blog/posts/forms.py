from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Post, Comment


class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    exclude = ["post"]
    labels = {
      "username": "Your Name:",
      "email": "Your Email Address:",
      "text": "Your Comment:",
    }


class PostForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        # fields = '__all__'
        exclude = ["slug"]
