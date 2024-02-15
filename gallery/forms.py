from django import forms
from .models import Image, Comment


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'image', 'description', 'category', 'uploaded_by']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {
            'text': 'Ваш комментарий',
        }
        error_messages = {
            'text': {
                'required': 'Это поле обязательно к заполнению'
            },
        }
