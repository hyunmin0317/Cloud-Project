from django import forms
from place.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'image']

        labels = {
            'content': '내용',
            'image': '사진',
        }