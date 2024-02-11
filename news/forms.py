from django import forms
from .models import Comment


class SearchForm(forms.Form):
    search = forms.CharField(max_length=256)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text_news', 'comment_author_news']
