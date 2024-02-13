from django import forms

from posts.models import Comment


class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    exclude = ["post"]
    labels = {
      "username": "Your Name:",
      "email": "Your Email Address:",
      "text": "Your Comment:",
    }