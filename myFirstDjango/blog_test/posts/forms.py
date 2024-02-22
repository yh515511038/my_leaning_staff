from django import forms


class CommentForm(forms.Form):
    username = forms.CharField(max_length=100)
    content = forms.CharField(max_length=300, widget=forms.Textarea)
